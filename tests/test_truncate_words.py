from textkit import truncate_words


def test_short_text_is_unchanged() -> None:
    assert truncate_words("one two", 2) == "one two"
    assert truncate_words("one two", 5) == "one two"


def test_long_text_is_cut_with_ellipsis() -> None:
    assert truncate_words("one two three four", 2) == "one two..."
