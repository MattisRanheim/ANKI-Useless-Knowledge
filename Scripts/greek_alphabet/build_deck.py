# -*- coding: utf-8 -*-
"""
Build the "Greek Alphabet for Mathematics" Anki deck (.apkg).

Front: the Greek symbol (e.g. δ, Σ, ϵ).
Back:  the English name, plus whether it's the upper/lower/variant form and the
       LaTeX command that produces it.

Run:  python3 Scripts/greek_alphabet/build_deck.py
"""

import os
import sys
import genanki

# Make the shared `common` package importable when run as a script.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.paths import deck_path

from letters_data import LETTERS

OUTPUT_FILE = deck_path("greek_alphabet.apkg")

# Stable IDs so re-running updates the same deck rather than duplicating it.
MODEL_ID = 1_846_203_751
DECK_ID  = 1_573_920_486

CSS = """
.card {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    text-align: center;
    background-color: #fcfcfa;
    color: #222;
    padding: 28px;
}
.symbol {
    font-family: 'Times New Roman', 'STIX Two Math', Georgia, serif;
    font-size: 110px;
    line-height: 1.0;
    color: #5a3fa0;
}
.name {
    font-size: 38px;
    font-weight: 600;
    margin-top: 14px;
    text-transform: capitalize;
}
.meta {
    font-size: 18px;
    color: #777;
    margin-top: 8px;
}
.latex {
    font-family: 'SF Mono', 'Menlo', Consolas, monospace;
    background: #f0eef7;
    color: #5a3fa0;
    padding: 1px 7px;
    border-radius: 4px;
}
hr {
    border: none;
    border-top: 1px solid #ddd;
    margin: 20px auto;
    width: 55%;
}
"""

FRONT_TMPL = '<div class="symbol">{{Symbol}}</div>'
BACK_TMPL = """\
{{FrontSide}}
<hr>
<div class="name">{{Name}}</div>
<div class="meta">{{Form}} &middot; <span class="latex">{{Latex}}</span></div>
"""

MODEL = genanki.Model(
    MODEL_ID,
    "Greek Letter Card",
    fields=[
        {"name": "Symbol"},
        {"name": "Name"},
        {"name": "Form"},
        {"name": "Latex"},
    ],
    templates=[{"name": "Symbol -> Name", "qfmt": FRONT_TMPL, "afmt": BACK_TMPL}],
    css=CSS,
)


def build_deck():
    deck = genanki.Deck(DECK_ID, "Greek Alphabet for Mathematics")
    for symbol, name, form, latex in LETTERS:
        note = genanki.Note(model=MODEL, fields=[symbol, name, form, latex])
        deck.add_note(note)
    return deck


def main():
    deck = build_deck()
    genanki.Package(deck).write_to_file(OUTPUT_FILE)

    n = len(LETTERS)
    lower = sum(1 for l in LETTERS if l[2] == "lowercase")
    upper = sum(1 for l in LETTERS if l[2] == "uppercase")
    variant = n - lower - upper
    print(f"\n{'='*50}")
    print("Deck: Greek Alphabet for Mathematics")
    print(f"Cards written: {n}  ({lower} lowercase, {upper} uppercase, {variant} variant forms)")
    print(f"Output: {OUTPUT_FILE}")
    print('='*50)


if __name__ == "__main__":
    main()
