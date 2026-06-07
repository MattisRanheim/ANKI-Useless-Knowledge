# -*- coding: utf-8 -*-
"""
Build the "250 Famous Movies" Anki deck (.apkg) from the IMDb Top 250.

Front: the movie title.
Back:  the release year (the answer), plus the director as context.

Run:  python3 Scripts/movies_top250/build_deck.py
"""

import os
import sys
import genanki

# Make the shared `common` package importable when run as a script.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.paths import deck_path

from movies_data import MOVIES

OUTPUT_FILE = deck_path("famous_movies.apkg")

# Stable IDs so re-running updates the same deck rather than duplicating it.
MODEL_ID = 1_772_038_495
DECK_ID  = 1_093_847_562

CSS = """
.card {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    text-align: center;
    background-color: #14171c;
    color: #f3f3f0;
    padding: 28px;
}
.title {
    font-size: 32px;
    font-weight: 700;
    line-height: 1.3;
    max-width: 92%;
    margin: 0 auto;
}
hr {
    border: none;
    border-top: 1px solid #3a3f47;
    margin: 22px auto;
    width: 55%;
}
.year {
    font-size: 52px;
    font-weight: 700;
    color: #f5c518;   /* IMDb yellow */
}
.director {
    font-size: 19px;
    color: #9aa0a6;
    margin-top: 10px;
}
.director-label {
    font-size: 13px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #6b7280;
}
"""

FRONT_TMPL = '<div class="title">{{Title}}</div>'
BACK_TMPL = """\
{{FrontSide}}
<hr>
<div class="year">{{Year}}</div>
<div class="director-label">directed by</div>
<div class="director">{{Director}}</div>
"""

MODEL = genanki.Model(
    MODEL_ID,
    "Famous Movie Card",
    fields=[
        {"name": "Title"},
        {"name": "Year"},
        {"name": "Director"},
    ],
    templates=[{"name": "Title -> Year", "qfmt": FRONT_TMPL, "afmt": BACK_TMPL}],
    css=CSS,
)


def build_deck():
    deck = genanki.Deck(DECK_ID, "250 Famous Movies (IMDb Top 250)")
    for title, year, director in MOVIES:
        note = genanki.Note(model=MODEL, fields=[title, str(year), director])
        deck.add_note(note)
    return deck


def main():
    deck = build_deck()
    genanki.Package(deck).write_to_file(OUTPUT_FILE)

    print(f"\n{'='*50}")
    print("Deck: 250 Famous Movies (IMDb Top 250)")
    print(f"Cards written: {len(MOVIES)}")
    print(f"Output: {OUTPUT_FILE}")
    print('='*50)


if __name__ == "__main__":
    main()
