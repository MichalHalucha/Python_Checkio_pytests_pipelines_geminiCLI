import pytest

from src.Find_Remainder import find_remainder


@pytest.mark.parametrize(
    "dividend, divisor, expected",
    [
        (10, 3, 1),
        (14, 4, 2),
        (27, 4, 3),
        (10, 5, 0),
        (10, 1, 0),
        (5, 7, 5),
        (7, 5, 2),
    ],
)
def test_find_remainder(dividend: int, divisor: int, expected: int) -> None:
    """Check that find_remainder returns the correct remainder for various integer pairs."""
    assert find_remainder(dividend, divisor) == expected
