from textkit import slugify


def test_basic() -> None:
    assert slugify("Hello World") == "hello-world"


def test_punctuation_and_spaces() -> None:
    assert slugify("  Aflvaki: tickets -> PRs!  ") == "aflvaki-tickets-prs"


def test_empty() -> None:
    assert slugify("") == ""
