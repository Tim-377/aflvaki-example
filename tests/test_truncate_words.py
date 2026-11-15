import pytest

from textkit import truncate_words


def test_truncate_words_fewer_words_unchanged() -> None:
    assert truncate_words("one two", 3) == "one two"


def test_truncate_words_exactly_n_words_unchanged() -> None:
    assert truncate_words("one two three", 3) == "one two three"


def test_truncate_words_unchanged_preserves_whitespace() -> None:
    assert truncate_words("  one  two ", 2) == "  one  two "


def test_truncate_words_empty() -> None:
    assert truncate_words("", 3) == ""


def test_truncate_words_longer_text() -> None:
    assert truncate_words("one two three four", 2) == "one two..."


def test_truncate_words_longer_text_collapses_whitespace() -> None:
    assert truncate_words("one  two\tthree\nfour", 3) == "one two three..."


def test_truncate_words_zero() -> None:
    assert truncate_words("one two", 0) == "..."


def test_truncate_words_negative_n_raises() -> None:
    with pytest.raises(ValueError):
        truncate_words("one two", -1)
