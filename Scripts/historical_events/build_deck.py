# -*- coding: utf-8 -*-
"""
Build the "Important Historical Events" Anki deck (.apkg).

Front: the historical event.
Back:  the date (the year, or the exact date when one is well-established).

Run:  python3 Scripts/historical_events/build_deck.py
"""

import os
import sys
import genanki

# Make the shared `common` package importable when run as a script.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.paths import deck_path

from events_data import EVENTS

OUTPUT_FILE = deck_path("historical_events.apkg")

# Stable IDs so re-running updates the same deck rather than duplicating it.
MODEL_ID = 1_583_920_647
DECK_ID  = 1_428_193_057

CSS = """
.card {
    font-family: Georgia, 'Times New Roman', serif;
    text-align: center;
    background-color: #f4efe6;
    color: #2b2620;
    padding: 26px;
}
.event {
    font-size: 30px;
    font-weight: bold;
    line-height: 1.35;
    max-width: 92%;
    margin: 0 auto;
}
hr {
    border: none;
    border-top: 1px solid #cabfa8;
    margin: 22px auto;
    width: 55%;
}
.date {
    font-size: 46px;
    font-weight: 700;
    color: #8a5a2b;
}
"""

FRONT_TMPL = '<div class="event">{{Event}}</div>'
BACK_TMPL = """\
{{FrontSide}}
<hr>
<div class="date">{{Date}}</div>
"""

MODEL = genanki.Model(
    MODEL_ID,
    "Historical Event Card",
    fields=[{"name": "Event"}, {"name": "Date"}],
    templates=[{"name": "Event -> Date", "qfmt": FRONT_TMPL, "afmt": BACK_TMPL}],
    css=CSS,
)


def build_deck():
    deck = genanki.Deck(DECK_ID, "Important Historical Events")
    for event, date in EVENTS:
        note = genanki.Note(model=MODEL, fields=[event, date])
        deck.add_note(note)
    return deck


def main():
    deck = build_deck()
    genanki.Package(deck).write_to_file(OUTPUT_FILE)

    print(f"\n{'='*50}")
    print("Deck: Important Historical Events")
    print(f"Cards written: {len(EVENTS)}")
    print(f"Output: {OUTPUT_FILE}")
    print('='*50)


if __name__ == "__main__":
    main()
