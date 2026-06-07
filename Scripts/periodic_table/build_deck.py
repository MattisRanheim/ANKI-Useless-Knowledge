# -*- coding: utf-8 -*-
"""
Build the "Periodic Table (1-88)" Anki deck (.apkg).

One note per element, with TWO card templates so you can study both directions
from the same data (no second deck needed):

  Card 1  "Symbol -> Name":   front = symbol      -> back = names + atomic number
  Card 2  "Number -> Element": front = atomic no.  -> back = symbol + names

That's 88 notes x 2 = 176 cards. If you only ever want one direction, you can
suspend or delete one of the two card types inside Anki.

Run:  python3 Scripts/periodic_table/build_deck.py
"""

import os
import sys
import genanki

# Make the shared `common` package importable when run as a script.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.paths import deck_path

from elements_data import ELEMENTS

OUTPUT_FILE = deck_path("periodic_table.apkg")

# Stable IDs so re-running updates the same deck rather than duplicating it.
MODEL_ID = 1_734_905_216
DECK_ID  = 1_209_384_756

CSS = """
.card {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    text-align: center;
    background-color: #f7f9fb;
    color: #1a2330;
    padding: 24px;
}
.prompt-label {
    font-size: 15px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #8a97a6;
    margin-bottom: 6px;
}
.symbol {
    font-size: 80px;
    font-weight: 700;
    line-height: 1.0;
    color: #1f6feb;
}
.symbol-sm {
    font-size: 52px;
    font-weight: 700;
    color: #1f6feb;
}
.number {
    font-size: 76px;
    font-weight: 700;
    color: #1f6feb;
}
.name-en {
    font-size: 32px;
    font-weight: 600;
    margin-top: 12px;
}
.name-la {
    font-size: 22px;
    font-style: italic;
    color: #5b6776;
    margin-top: 4px;
}
.atomic {
    font-size: 19px;
    color: #5b6776;
    margin-top: 10px;
}
hr {
    border: none;
    border-top: 1px solid #d4dbe2;
    margin: 20px auto;
    width: 55%;
}
"""

# Card 1: see the symbol, recall the element.
SYMBOL_FRONT = """\
<div class="prompt-label">Symbol</div>
<div class="symbol">{{Symbol}}</div>
"""
SYMBOL_BACK = """\
{{FrontSide}}
<hr>
<div class="name-en">{{English}}</div>
<div class="name-la">Latin: {{Latin}}</div>
<div class="atomic">Atomic number {{Number}}</div>
"""

# Card 2: see the atomic number, recall the symbol and name.
NUMBER_FRONT = """\
<div class="prompt-label">Atomic number</div>
<div class="number">{{Number}}</div>
"""
NUMBER_BACK = """\
{{FrontSide}}
<hr>
<div class="symbol-sm">{{Symbol}}</div>
<div class="name-en">{{English}}</div>
<div class="name-la">Latin: {{Latin}}</div>
"""

MODEL = genanki.Model(
    MODEL_ID,
    "Periodic Table Element",
    fields=[
        {"name": "Number"},
        {"name": "Symbol"},
        {"name": "English"},
        {"name": "Latin"},
    ],
    templates=[
        {"name": "Symbol -> Name",    "qfmt": SYMBOL_FRONT, "afmt": SYMBOL_BACK},
        {"name": "Number -> Element", "qfmt": NUMBER_FRONT, "afmt": NUMBER_BACK},
    ],
    css=CSS,
)


def build_deck():
    deck = genanki.Deck(DECK_ID, "Periodic Table (1-88)")
    for number, symbol, english, latin in ELEMENTS:
        note = genanki.Note(
            model=MODEL,
            fields=[str(number), symbol, english, latin],
        )
        deck.add_note(note)
    return deck


def main():
    deck = build_deck()
    genanki.Package(deck).write_to_file(OUTPUT_FILE)

    n = len(ELEMENTS)
    print(f"\n{'='*50}")
    print("Deck: Periodic Table (1-88)")
    print(f"Elements (notes): {n}")
    print(f"Cards written: {n * 2}  (2 per element: symbol->name, number->element)")
    print(f"Output: {OUTPUT_FILE}")
    print('='*50)


if __name__ == "__main__":
    main()
