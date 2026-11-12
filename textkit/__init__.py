"""Small text utilities."""

import re


def word_count(text: str) -> int:
    """Count whitespace-separated words."""
    return len(text.split())


def slugify(text: str) -> str:
    """Lowercase, join runs of non-alphanumerics with one dash, trim dashes."""
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
