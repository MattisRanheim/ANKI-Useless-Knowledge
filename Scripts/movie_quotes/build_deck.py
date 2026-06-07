# -*- coding: utf-8 -*-
"""
Build the "Famous Movie Quotes" Anki deck (.apkg).

Front: the quote.
Back:  the movie (with year), the character, and the actor who played them.

Run:  python3 Scripts/movie_quotes/build_deck.py
"""

import os
import sys
import genanki

# Make the shared `common` package importable when run as a script.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.paths import deck_path

from quotes_data import QUOTES

OUTPUT_FILE = deck_path("movie_quotes.apkg")

# Stable IDs so re-running updates the same deck rather than duplicating it.
MODEL_ID = 1_657_483_920
DECK_ID  = 1_390_847_265

CSS = """
.card {
    font-family: Georgia, 'Times New Roman', serif;
    text-align: center;
    background-color: #fbfaf7;
    color: #1a1a1a;
    padding: 24px;
}
.quote {
    font-size: 30px;
    font-style: italic;
    line-height: 1.4;
    max-width: 90%;
    margin: 0 auto;
}
hr {
    border: none;
    border-top: 1px solid #ccc;
    margin: 22px auto;
    width: 55%;
}
.movie {
    font-size: 27px;
    font-weight: bold;
    margin-top: 8px;
}
.year {
    font-weight: normal;
    color: #777;
}
.role {
    font-size: 19px;
    color: #444;
    margin-top: 10px;
}
.actor {
    color: #777;
    font-style: italic;
}
"""

# Front shows the quote in big curly quotation marks; back adds the answer.
FRONT_TMPL = '<div class="quote">&ldquo;{{Quote}}&rdquo;</div>'
BACK_TMPL = """\
{{FrontSide}}
<hr>
<div class="movie">{{Movie}} <span class="year">({{Year}})</span></div>
<div class="role">{{Character}} &middot; <span class="actor">played by {{Actor}}</span></div>
"""

MODEL = genanki.Model(
    MODEL_ID,
    "Movie Quote Card",
    fields=[
        {"name": "Quote"},
        {"name": "Movie"},
        {"name": "Year"},
        {"name": "Character"},
        {"name": "Actor"},
    ],
    templates=[{"name": "Movie Quote", "qfmt": FRONT_TMPL, "afmt": BACK_TMPL}],
    css=CSS,
)


def build_deck():
    deck = genanki.Deck(DECK_ID, "Famous Movie Quotes")
    for quote, movie, year, character, actor in QUOTES:
        note = genanki.Note(
            model=MODEL,
            fields=[quote, movie, str(year), character, actor],
        )
        deck.add_note(note)
    return deck


def main():
    deck = build_deck()
    genanki.Package(deck).write_to_file(OUTPUT_FILE)

    print(f"\n{'='*50}")
    print("Deck: Famous Movie Quotes")
    print(f"Cards written: {len(QUOTES)}")
    print(f"Output: {OUTPUT_FILE}")
    print('='*50)


if __name__ == "__main__":
    main()
