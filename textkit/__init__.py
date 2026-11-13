"""Small text utilities."""

import re


def word_count(text: str) -> int:
    """Count whitespace-separated words."""
    return len(text.split())


def slugify(text: str) -> str:
    """Lowercase, join runs of non-alphanumerics with one dash, trim dashes."""
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def truncate_words(text: str, n: int) -> str:
    """Keep the first n words; append '...' when words were cut."""
    words = text.split()
    if len(words) <= n:
        return text
    return " ".join(words[:n]) + "..."
