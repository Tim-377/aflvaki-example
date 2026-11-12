from textkit import word_count


def test_word_count() -> None:
    assert word_count("one two  three") == 3


def test_word_count_empty() -> None:
    assert word_count("") == 0
