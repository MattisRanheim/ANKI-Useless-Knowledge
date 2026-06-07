"""
Build the Anki deck (.apkg) from the generated constellation charts.

Run generate_charts.py first to produce the label-free star charts in ./images/.
This script packages them into cards (chart on front, EN/SV names on back).
"""

import os
import sys
import genanki

# Make the shared `common` package importable when run as a script.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.paths import images_dir, deck_path

IMAGES_DIR = images_dir("constellations")
OUTPUT_FILE = deck_path("constellations.apkg")

# Stable IDs so re-runs update the same deck rather than duplicate it.
MODEL_ID = 1_482_930_571
DECK_ID  = 2_093_847_162

# (English name, Swedish name, image filename in ./images/)
CONSTELLATIONS = [
    ("Orion",       "Orion",         "Orion.png"),
    ("Ursa Major",  "Stora björnen", "Ursa_Major.png"),
    ("Ursa Minor",  "Lilla björnen", "Ursa_Minor.png"),
    ("Cassiopeia",  "Cassiopeja",    "Cassiopeia.png"),
    ("Leo",         "Lejonet",       "Leo.png"),
    ("Taurus",      "Oxen",          "Taurus.png"),
    ("Gemini",      "Tvillingarna",  "Gemini.png"),
    ("Scorpius",    "Skorpionen",    "Scorpius.png"),
    ("Sagittarius", "Skytten",       "Sagittarius.png"),
    ("Cancer",      "Kräftan",       "Cancer.png"),
    ("Aries",       "Väduren",       "Aries.png"),
    ("Virgo",       "Jungfrun",      "Virgo.png"),
    ("Cygnus",      "Svanen",        "Cygnus.png"),
    ("Draco",       "Draken",        "Draco.png"),
    ("Canis Major", "Stora hunden",  "Canis_Major.png"),
    ("Andromeda",   "Andromeda",     "Andromeda.png"),
    ("Perseus",     "Perseus",       "Perseus.png"),
    ("Lyra",        "Lyran",         "Lyra.png"),
    ("Aquila",      "Örnen",         "Aquila.png"),
    ("Pegasus",     "Pegasus",       "Pegasus.png"),
]

# ── Anki model ───────────────────────────────────────────────────────────────

CSS = """
.card {
    font-family: Arial, sans-serif;
    text-align: center;
    background-color: white;
    padding: 16px;
}
img {
    max-width: 90%;
    height: auto;
    border-radius: 6px;
}
.english {
    font-size: 32px;
    font-weight: bold;
    margin-top: 16px;
}
.swedish {
    font-size: 24px;
    color: #555;
    margin-top: 6px;
}
hr {
    border: none;
    border-top: 1px solid #ccc;
    margin: 16px auto;
    width: 60%;
}
"""

# Anki scans field values (not templates) for media references, so the Image
# field stores the full <img> tag and the template just renders it.
FRONT_TMPL = "{{Image}}"
BACK_TMPL = """\
{{FrontSide}}
<hr>
<div class="english">{{English}}</div>
<div class="swedish">{{Swedish}}</div>
"""

MODEL = genanki.Model(
    MODEL_ID,
    "Constellation Card",
    fields=[{"name": "Image"}, {"name": "English"}, {"name": "Swedish"}],
    templates=[{"name": "Constellation", "qfmt": FRONT_TMPL, "afmt": BACK_TMPL}],
    css=CSS,
)


def build_deck():
    """Build the deck from chart images present in ./images/."""
    deck = genanki.Deck(DECK_ID, "Famous Constellations (EN/SV)")
    media_files, missing = [], []

    for english, swedish, filename in CONSTELLATIONS:
        path = os.path.join(IMAGES_DIR, filename)
        if not (os.path.exists(path) and os.path.getsize(path) > 5_000):
            print(f"  [MISSING IMAGE] {english} -> {filename}; skipping")
            missing.append(english)
            continue

        note = genanki.Note(
            model=MODEL,
            # Full <img> tag in the field so Anki imports the media on import.
            fields=[f'<img src="{filename}">', english, swedish],
        )
        deck.add_note(note)
        media_files.append(path)

    package = genanki.Package(deck)
    package.media_files = media_files
    return package, len(media_files), missing


def main():
    package, card_count, missing = build_deck()
    package.write_to_file(OUTPUT_FILE)

    print(f"\n{'='*50}")
    print("Deck: Famous Constellations (EN/SV)")
    print(f"Cards written: {card_count}")
    print(f"Output: {OUTPUT_FILE}")
    if missing:
        print(f"\nMissing images ({len(missing)}): {', '.join(missing)}")
        print("Run generate_charts.py to create them.")
    else:
        print("All 20 charts included.")
    print('='*50)


if __name__ == "__main__":
    main()
