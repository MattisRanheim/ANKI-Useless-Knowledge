# -*- coding: utf-8 -*-
"""
Build the "Famous Inventions" Anki deck (.apkg).

Front: the invention.
Back:  the inventor and the year of invention.

Run:  python3 Scripts/inventions/build_deck.py
"""

import os
import sys
import genanki

# Make the shared `common` package importable when run as a script.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.paths import deck_path

from inventions_data import INVENTIONS

OUTPUT_FILE = deck_path("inventions.apkg")

# Stable IDs so re-running updates the same deck rather than duplicating it.
MODEL_ID = 1_925_374_860
DECK_ID  = 1_648_209_357

CSS = """
.card {
    font-family: Georgia, 'Times New Roman', serif;
    text-align: center;
    background-color: #fbf9f4;
    color: #2a2520;
    padding: 26px;
}
.invention {
    font-size: 34px;
    font-weight: bold;
    line-height: 1.3;
    max-width: 90%;
    margin: 0 auto;
}
hr {
    border: none;
    border-top: 1px solid #d8d2c4;
    margin: 22px auto;
    width: 55%;
}
.inventor {
    font-size: 26px;
    font-weight: 600;
}
.year {
    font-size: 22px;
    color: #8a6d3b;
    margin-top: 8px;
    letter-spacing: 0.02em;
}
"""

FRONT_TMPL = '<div class="invention">{{Invention}}</div>'
BACK_TMPL = """\
{{FrontSide}}
<hr>
<div class="inventor">{{Inventor}}</div>
<div class="year">{{Year}}</div>
"""

MODEL = genanki.Model(
    MODEL_ID,
    "Invention Card",
    fields=[
        {"name": "Invention"},
        {"name": "Inventor"},
        {"name": "Year"},
    ],
    templates=[{"name": "Invention -> Inventor & Year", "qfmt": FRONT_TMPL, "afmt": BACK_TMPL}],
    css=CSS,
)


def build_deck():
    deck = genanki.Deck(DECK_ID, "Famous Inventions")
    for invention, inventor, year in INVENTIONS:
        note = genanki.Note(model=MODEL, fields=[invention, inventor, year])
        deck.add_note(note)
    return deck


def main():
    deck = build_deck()
    genanki.Package(deck).write_to_file(OUTPUT_FILE)

    print(f"\n{'='*50}")
    print("Deck: Famous Inventions")
    print(f"Cards written: {len(INVENTIONS)}")
    print(f"Output: {OUTPUT_FILE}")
    print('='*50)


if __name__ == "__main__":
    main()
