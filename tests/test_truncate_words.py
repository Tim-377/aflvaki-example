from textkit import truncate_words

def test_truncate_words_short() -> None:
    assert truncate_words("one two three", 3) == "one two three"

def test_truncate_words_long() -> None:
    assert truncate_words("one two three four five six", 3) == "one two three..."
