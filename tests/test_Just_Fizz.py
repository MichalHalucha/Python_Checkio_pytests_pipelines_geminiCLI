import pytest

from src.Just_Fizz import checkio


@pytest.mark.parametrize(
    ("input", "output"),
    [
        (15, "Fizz"),
        (6, "Fizz"),
        (10, "10"),
        (7, "7"),
    ],
)
def test_just_fizz(input: int, output: str):
    assert checkio(input) == output
