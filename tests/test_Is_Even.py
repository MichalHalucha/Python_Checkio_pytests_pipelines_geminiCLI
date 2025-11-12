import pytest

from src.Is_Even import is_even


@pytest.mark.parametrize(
    "num, expected",
    [
        (0, True),
        (1, False),
        (2, True),
        (3, False),
        (4, True),
        (99, False),
        (100, True),
        (-1, False),
        (-2, True),
        (-101, False),
        (-200, True),
    ],
    ids=[
        "zero",
        "one",
        "two",
        "three",
        "four",
        "odd_99",
        "even_100",
        "neg_1",
        "neg_2",
        "neg_odd_101",
        "neg_even_200",
    ],
)
def test_is_even_parametrized(num, expected):
    assert is_even(num) == expected
