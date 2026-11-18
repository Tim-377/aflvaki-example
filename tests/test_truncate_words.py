from textkit import truncate_words


def test_truncate_words_short_text_unchanged() -> None:
    assert truncate_words("one two", 3) == "one two"


def test_truncate_words_exact_length_unchanged() -> None:
    assert truncate_words("one  two three", 3) == "one  two three"


def test_truncate_words_long_text() -> None:
    assert truncate_words("one two three four five", 3) == "one two three..."
