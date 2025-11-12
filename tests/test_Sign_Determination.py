import pytest

from src.Integer_Sign_Determination import determine_sign


@pytest.mark.parametrize(
    "a, expected",
    [
        (5, "positive"),
        (0, "zero"),
        (-10, "negative"),
        (999, "positive"),
        (-1000, "negative"),
    ],
)
def test_mult_two_parametrized(a, expected):
    assert determine_sign(a) == expected
