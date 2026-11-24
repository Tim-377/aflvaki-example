"""Small text utilities."""

import re


def word_count(text: str) -> int:
    """Count whitespace-separated words."""
    return len(text.split())


def slugify(text: str) -> str:
    """Lowercase, join runs of non-alphanumerics with one dash, trim dashes."""
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def truncate_words(text: str, n: int) -> str:
    """Keep the first ``n`` whitespace-separated words of ``text``.

    If ``text`` has ``n`` words or fewer it is returned unchanged. Otherwise
    the first ``n`` words are joined with single spaces and ``"..."`` is
    appended. Raises ``ValueError`` if ``n`` is negative.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    words = text.split()
    if len(words) <= n:
        return text
    return " ".join(words[:n]) + "..."
