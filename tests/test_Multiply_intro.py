import pytest

from src.Multiply_intro import mult_two


def test_mult_two_basic_cases():
    assert mult_two(2, 3) == 6
    assert mult_two(-2, 3) == -6
    assert mult_two(0, 99) == 0
    assert mult_two(7, 1) == 7
    assert mult_two(1, 7) == 7

def test_mult_two_large_numbers():
    assert mult_two(10**6, 10**6) == 10**12

def test_mult_two_returns_int():
    result = mult_two(2, 3)
    assert isinstance(result, int)

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),
        (-1, 5, -5),
        (0, 9, 0),
        (100, -2, -200),
        (7, 7, 49),
    ],
)
def test_mult_two_parametrized(a, b, expected):
    assert mult_two(a, b) == expected
