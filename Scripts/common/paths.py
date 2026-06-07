"""
Shared path helpers for all deck-building scripts.

Resolves the repo's standard folders relative to this file, so scripts work
no matter the current working directory:

    <repo>/
        ANKI Decks/        finished .apkg files
        Resources/
            Images/        per-deck image folders
            catalogs/      cached data catalogs (e.g. Hipparcos)
        Scripts/           the build scripts (this lives in Scripts/common/)
"""

import os

# Scripts/common/paths.py -> repo root is two levels up from this file's dir.
REPO_ROOT     = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

DECKS_DIR     = os.path.join(REPO_ROOT, "ANKI Decks")
RESOURCES_DIR = os.path.join(REPO_ROOT, "Resources")
IMAGES_DIR    = os.path.join(RESOURCES_DIR, "Images")
CATALOGS_DIR  = os.path.join(RESOURCES_DIR, "catalogs")


def deck_path(filename: str) -> str:
    """Absolute path for an output .apkg in the ANKI Decks folder."""
    os.makedirs(DECKS_DIR, exist_ok=True)
    return os.path.join(DECKS_DIR, filename)


def images_dir(deck_name: str) -> str:
    """Absolute path to a per-deck image folder, created if missing."""
    path = os.path.join(IMAGES_DIR, deck_name)
    os.makedirs(path, exist_ok=True)
    return path


def catalogs_dir() -> str:
    """Absolute path to the cached-catalogs folder, created if missing."""
    os.makedirs(CATALOGS_DIR, exist_ok=True)
    return CATALOGS_DIR
