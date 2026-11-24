import pytest

from textkit import truncate_words


def test_truncate_words_short_text_unchanged() -> None:
    assert truncate_words("one two  three", 3) == "one two  three"
    assert truncate_words("one two", 5) == "one two"


def test_truncate_words_empty() -> None:
    assert truncate_words("", 2) == ""


def test_truncate_words_cuts_and_appends_ellipsis() -> None:
    assert truncate_words("one two three four", 2) == "one two..."


def test_truncate_words_zero() -> None:
    assert truncate_words("one two", 0) == "..."


def test_truncate_words_negative_raises() -> None:
    with pytest.raises(ValueError):
        truncate_words("one two", -1)
