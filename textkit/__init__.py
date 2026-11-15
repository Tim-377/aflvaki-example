"""Small text utilities."""

import re


def word_count(text: str) -> int:
    """Count whitespace-separated words."""
    return len(text.split())


def slugify(text: str) -> str:
    """Lowercase, join runs of non-alphanumerics with one dash, trim dashes."""
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def truncate_words(text: str, n: int) -> str:
    """Keep at most the first n whitespace-separated words.

    Text with n words or fewer is returned unchanged. Longer text is cut to
    its first n words, joined by single spaces and followed by '...'.
    Raises ValueError if n is negative.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    words = text.split()
    if len(words) <= n:
        return text
    return " ".join(words[:n]) + "..."
