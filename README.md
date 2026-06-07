# ANKI: Useless Knowledge

A small collection of Python-generated [Anki](https://apps.ankiweb.net/) flashcard
decks for memorizing delightfully non-essential trivia — constellations, movie
quotes, the periodic table, Greek letters, famous inventions, the greatest films,
and the turning points of world history.

Every deck is built programmatically with [`genanki`](https://github.com/kerrickstaley/genanki),
so the data lives in plain Python files and the `.apkg` files are reproducible.

## The decks

Pre-built `.apkg` files live in [`ANKI Decks/`](ANKI%20Decks) — download one and
open it in Anki (**File → Import**, or just double-click).

| Deck | Cards | Front → Back |
|------|------:|--------------|
| **Famous Constellations (EN/SV)** | 20 | Unlabeled star chart → name in English & Swedish |
| **Famous Movie Quotes** | 250 | The quote → movie, year, character & actor |
| **Periodic Table (1–88)** | 176 | Symbol → name + atomic number, **and** atomic number → element |
| **Greek Alphabet for Mathematics** | 40 | Greek symbol → English name (+ LaTeX) |
| **Famous Inventions** | 163 | The invention → inventor + year |
| **250 Famous Movies (IMDb Top 250)** | 250 | Film title → release year + director |
| **Important Historical Events** | 211 | The event → date (exact date where defined) |

*~1,110 cards in total.*

The Periodic Table deck is a good example of a single note type with **two card
templates**, giving you two study directions from the same data without a second
deck.

## Repository structure

```
ANKI: Useless Knowledge/
├── ANKI Decks/             # Finished .apkg files (the deliverables)
├── Resources/
│   ├── Images/             # Per-deck image assets (e.g. constellation charts)
│   └── catalogs/           # Cached data catalogs — git-ignored, re-downloaded on demand
└── Scripts/
    ├── common/paths.py     # Shared folder paths, resolved from the repo root
    ├── constellations/     # generate_charts.py + build_deck.py
    ├── movie_quotes/
    ├── periodic_table/
    ├── greek_alphabet/
    ├── inventions/
    ├── movies_top250/
    ├── historical_events/
    └── README.md           # Developer notes: how the build works, how to add a deck
```

## Building from source

```bash
pip install genanki requests                 # core
pip install skyfield pandas matplotlib numpy # only for the constellations deck

# Build any deck — output lands in "ANKI Decks/"
python3 Scripts/movie_quotes/build_deck.py
python3 Scripts/periodic_table/build_deck.py
python3 Scripts/historical_events/build_deck.py
# ...etc

# The constellations deck generates its images first:
python3 Scripts/constellations/generate_charts.py
python3 Scripts/constellations/build_deck.py
```

Each builder uses a hardcoded, stable deck/model ID, so re-running **updates** the
existing deck on import rather than creating a duplicate. See
[`Scripts/README.md`](Scripts/README.md) for the developer guide and the table of
IDs already in use.

## Sources & accuracy

The data is curated from authoritative sources, with a few documented judgment
calls (approximate ancient dates, contested inventor/quote attributions, original
vs. wide-release film years, etc.):

- **Constellations** — star positions from the Hipparcos catalog; constellation
  lines from Stellarium's modern sky culture. Charts are generated, label-free.
- **Movie Quotes** — AFI's *100 Years…100 Movie Quotes* plus 150 widely
  celebrated lines.
- **Famous Movies** — the [IMDb Top 250](https://www.imdb.com/chart/top/), with
  foreign titles mapped to their English names and years corrected to the
  canonical original-release year.
- **Inventions** — Wikipedia's *Timeline of historic inventions* and standard
  attribution histories.
- **Historical Events** — well-established dates across all eras and regions.
- **Periodic Table / Greek Alphabet** — standard references; Latin element names
  use the New Latin (scientific) forms.

## License

The build code is free to use and adapt. Card content is compiled from public
factual sources for educational use; trademarks and quoted material belong to
their respective owners.

---

*Built with [Claude Code](https://claude.com/claude-code).*
