"""
Generate clean, label-free constellation star charts.

Star positions come from the Hipparcos catalog (via skyfield); the constellation
stick-figure lines come from Stellarium's modern sky culture (index.json), which
stores each constellation's lines as polylines of HIP catalog numbers.

Output: one square PNG per constellation in Resources/Images/constellations/.
"""

import os
import sys
import math
import json
import requests
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from skyfield.api import Loader
from skyfield.data import hipparcos

# Make the shared `common` package importable when run as a script.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.paths import images_dir, catalogs_dir

IMAGES_DIR = images_dir("constellations")
HEADERS = {"User-Agent": "ConstellationDeckBuilder/1.0 (educational use)"}
STELLARIUM_URL = (
    "https://raw.githubusercontent.com/Stellarium/stellarium/master"
    "/skycultures/modern/index.json"
)

# (English name, IAU abbreviation, output filename)
CONSTELLATIONS = [
    ("Orion",       "Ori", "Orion.png"),
    ("Ursa Major",  "UMa", "Ursa_Major.png"),
    ("Ursa Minor",  "UMi", "Ursa_Minor.png"),
    ("Cassiopeia",  "Cas", "Cassiopeia.png"),
    ("Leo",         "Leo", "Leo.png"),
    ("Taurus",      "Tau", "Taurus.png"),
    ("Gemini",      "Gem", "Gemini.png"),
    ("Scorpius",    "Sco", "Scorpius.png"),
    ("Sagittarius", "Sgr", "Sagittarius.png"),
    ("Cancer",      "Cnc", "Cancer.png"),
    ("Aries",       "Ari", "Aries.png"),
    ("Virgo",       "Vir", "Virgo.png"),
    ("Cygnus",      "Cyg", "Cygnus.png"),
    ("Draco",       "Dra", "Draco.png"),
    ("Canis Major", "CMa", "Canis_Major.png"),
    ("Andromeda",   "And", "Andromeda.png"),
    ("Perseus",     "Per", "Perseus.png"),
    ("Lyra",        "Lyr", "Lyra.png"),
    ("Aquila",      "Aql", "Aquila.png"),
    ("Pegasus",     "Peg", "Pegasus.png"),
]

# ── Style ─────────────────────────────────────────────────────────────────────
BG_COLOR    = "#070718"   # deep night-sky blue
LINE_COLOR  = "#6fa8c7"   # soft constellation-line blue
STAR_COLOR  = "#ffffff"
FIELD_COLOR = "#9aa6c4"   # faint background field stars
FIELD_MAGLIM = 6.5        # how faint background stars go
PAD_FRAC    = 0.18        # padding around the figure as fraction of span


def load_constellation_lines() -> dict:
    """Return {abbrev: [[hip, hip, ...], ...]} polylines from Stellarium."""
    r = requests.get(STELLARIUM_URL, headers=HEADERS, timeout=30)
    r.raise_for_status()
    data = r.json()
    out = {}
    for c in data["constellations"]:
        abbrev = c["id"].split()[-1]   # "CON modern Ori" -> "Ori"
        out[abbrev] = c.get("lines", [])
    return out


def unwrap_ra(ra_deg, center):
    """Shift RA into (center-180, center+180] to handle the 0h/360 wrap."""
    return ((ra_deg - center + 180.0) % 360.0) - 180.0 + center


def star_sizes(mags):
    """Marker area scaled by brightness (brighter = bigger)."""
    m = np.clip(mags, -1.5, 7.0)
    return np.clip((7.0 - m), 0.4, None) ** 2.1 * 4.0


def generate_chart(abbrev, lines, stars_df, out_path):
    """Render one constellation chart. Returns True on success."""
    hip_ids = sorted({h for poly in lines for h in poly})
    if not hip_ids:
        print(f"  [NO LINE DATA] {abbrev}")
        return False

    # Positions of the stars that make up the figure.
    present = [h for h in hip_ids if h in stars_df.index]
    if len(present) < 2:
        print(f"  [MISSING STARS] {abbrev}")
        return False

    fig_ra  = stars_df.loc[present, "ra_degrees"].to_numpy()
    fig_dec = stars_df.loc[present, "dec_degrees"].to_numpy()

    # Center & unwrap so the figure is contiguous even across RA=0.
    dec_center = float(np.mean(fig_dec))
    # circular mean of RA for the wrap reference
    ra_rad = np.radians(fig_ra)
    ra_center = math.degrees(math.atan2(np.mean(np.sin(ra_rad)),
                                        np.mean(np.cos(ra_rad)))) % 360.0
    cosd = math.cos(math.radians(dec_center))

    def project(ra, dec):
        ra_u = unwrap_ra(ra, ra_center)
        x = -(ra_u - ra_center) * cosd   # negate: RA increases to the left
        y = dec - dec_center
        return x, y

    fx, fy = project(fig_ra, fig_dec)

    # Square bounding box with padding.
    span = max(fx.max() - fx.min(), fy.max() - fy.min())
    span = max(span, 2.0)
    pad = span * PAD_FRAC
    half = span / 2.0 + pad
    cx = (fx.max() + fx.min()) / 2.0
    cy = (fy.max() + fy.min()) / 2.0

    # Background field stars within the box.
    all_ra  = stars_df["ra_degrees"].to_numpy()
    all_dec = stars_df["dec_degrees"].to_numpy()
    all_mag = stars_df["magnitude"].to_numpy()
    bx, by = project(all_ra, all_dec)
    in_box = (
        (bx >= cx - half) & (bx <= cx + half) &
        (by >= cy - half) & (by <= cy + half) &
        (all_mag <= FIELD_MAGLIM)
    )

    fig, ax = plt.subplots(figsize=(6, 6), facecolor=BG_COLOR)
    ax.set_facecolor(BG_COLOR)

    # Background field stars (faint).
    ax.scatter(bx[in_box], by[in_box], s=star_sizes(all_mag[in_box]) * 0.6,
               c=FIELD_COLOR, alpha=0.55, edgecolors="none", zorder=1)

    # Constellation lines (each polyline drawn as a connected path).
    for poly in lines:
        pts = [project(stars_df.loc[h, "ra_degrees"], stars_df.loc[h, "dec_degrees"])
               for h in poly if h in stars_df.index]
        if len(pts) >= 2:
            xs, ys = zip(*pts)
            ax.plot(xs, ys, color=LINE_COLOR, lw=1.4, alpha=0.55, zorder=2,
                    solid_capstyle="round")

    # Glow halos behind the brightest figure stars.
    fig_mag = stars_df.loc[present, "magnitude"].to_numpy()
    bright = fig_mag < 2.5
    if bright.any():
        ax.scatter(fx[bright], fy[bright], s=star_sizes(fig_mag[bright]) * 4.0,
                   c=STAR_COLOR, alpha=0.18, edgecolors="none", zorder=3)

    # Main figure stars.
    ax.scatter(fx, fy, s=star_sizes(fig_mag), c=STAR_COLOR,
               edgecolors="none", zorder=4)

    ax.set_xlim(cx - half, cx + half)
    ax.set_ylim(cy - half, cy + half)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.tight_layout(pad=0)
    fig.savefig(out_path, dpi=110, facecolor=BG_COLOR,
                bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)
    return True


def main():
    os.makedirs(IMAGES_DIR, exist_ok=True)

    print("Loading Hipparcos star catalog...")
    # Cache the catalog under Resources/catalogs so re-runs don't re-download.
    load = Loader(catalogs_dir())
    with load.open(hipparcos.URL) as f:
        stars_df = hipparcos.load_dataframe(f)
    stars_df = stars_df[stars_df["magnitude"].notna()]
    print(f"  {len(stars_df):,} stars loaded.")

    print("Loading constellation line data...")
    lines_by_abbrev = load_constellation_lines()
    print(f"  {len(lines_by_abbrev)} constellations available.\n")

    ok, failed = [], []
    for english, abbrev, filename in CONSTELLATIONS:
        out_path = os.path.join(IMAGES_DIR, filename)
        lines = lines_by_abbrev.get(abbrev, [])
        print(f"  Drawing {english} ({abbrev}) ...", end=" ", flush=True)
        if generate_chart(abbrev, lines, stars_df, out_path):
            print(f"OK ({os.path.getsize(out_path)//1024} KB)")
            ok.append(english)
        else:
            print("FAILED")
            failed.append(english)

    print(f"\nGenerated {len(ok)}/{len(CONSTELLATIONS)} charts.")
    if failed:
        print("Failed:", ", ".join(failed))


if __name__ == "__main__":
    main()
