import pytest

from src.First_Word_Simplified import first_word


@pytest.mark.parametrize(
    ("input", "output"),
    [
        ("Hello world", "Hello"),
        ("a word", "a"),
        ("greeting from CheckiO Planet", "greeting"),
        ("hi", "hi"),
    ],
)
def test_first_word(input: str, output: str) -> None:
    assert first_word(input) == output
