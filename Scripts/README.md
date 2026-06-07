# Anki Deck Builders

A small toolkit for generating Anki decks (`.apkg`) with Python + [`genanki`].

## Repository layout

```
ANKI Decks/                 Finished .apkg files (the deliverables)
Resources/
    Images/
        constellations/     Generated star-chart PNGs
    catalogs/               Cached data catalogs (e.g. Hipparcos hip_main.dat)
Scripts/
    common/
        paths.py            Shared folder paths (resolved from repo root)
    constellations/
        generate_charts.py  Renders label-free star charts
        build_deck.py       Packages charts -> constellations.apkg
    movie_quotes/
        quotes_data.py      The 250 quotes (data only)
        build_deck.py       Packages quotes -> movie_quotes.apkg
    periodic_table/
        elements_data.py    The first 88 elements (data only)
        build_deck.py       Packages elements -> periodic_table.apkg
    greek_alphabet/
        letters_data.py     Greek letters used in math (data only)
        build_deck.py       Packages letters -> greek_alphabet.apkg
    inventions/
        inventions_data.py  Famous inventions, prehistory->today (data only)
        build_deck.py       Packages inventions -> inventions.apkg
    movies_top250/
        movies_data.py      IMDb Top 250 films + year + director (data only)
        build_deck.py       Packages movies -> famous_movies.apkg
    historical_events/
        events_data.py      ~210 major world-history events + dates (data only)
        build_deck.py       Packages events -> historical_events.apkg
```

## Setup

```bash
pip install genanki requests          # core
pip install skyfield pandas \
            matplotlib numpy           # only needed for the constellations deck
```

## Building the decks

```bash
# Movie quotes (no images, no network needed)
python3 Scripts/movie_quotes/build_deck.py

# Constellations (downloads star catalog + Stellarium line data on first run)
python3 Scripts/constellations/generate_charts.py
python3 Scripts/constellations/build_deck.py
```

Output `.apkg` files land in `ANKI Decks/`. Import them into Anki with
**File → Import** (or double-click).

## Adding a new deck

1. Create `Scripts/<your_deck>/`.
2. In your build script, make the shared helpers importable and use them for paths:

   ```python
   import os, sys
   sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
   from common.paths import deck_path, images_dir   # images_dir only if you need media

   OUTPUT_FILE = deck_path("your_deck.apkg")
   ```

3. Pick **stable, unique** 10-digit `MODEL_ID` and `DECK_ID` integers and hardcode
   them — this lets re-runs update the same deck instead of duplicating it.
   IDs already in use:

   | Deck            | MODEL_ID    | DECK_ID     |
   |-----------------|-------------|-------------|
   | Constellations  | 1482930571  | 2093847162  |
   | Movie Quotes    | 1657483920  | 1390847265  |
   | Periodic Table  | 1734905216  | 1209384756  |
   | Greek Alphabet  | 1846203751  | 1573920486  |
   | Famous Inventions | 1925374860 | 1648209357  |
   | Famous Movies   | 1772038495  | 1093847562  |
   | Historical Events | 1583920647 | 1428193057  |

A note type can define **multiple card templates** (see `periodic_table/`),
which generates several cards per note — handy for studying the same facts in
more than one direction without building a second deck.

4. If your cards use images, save them under `images_dir("your_deck")`, register
   them via `package.media_files = [...paths...]`, and reference them in the card
   template by **bare filename** inside an `<img>` tag stored in a note field
   (Anki scans field values, not templates, to discover media).

[`genanki`]: https://github.com/kerrickstaley/genanki
