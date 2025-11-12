import pytest

from src.Rectangle_perimeter import rectangle_perimeter


# --- Fixtura z zestawami danych (różne przypadki, w tym float) ---
@pytest.fixture
def rectangles():
    return [
        (2, 4),
        (3, 5),
        (10, 20),
        (7, 2),
        (1, 1),
        (1, 5),
        (4, 1),
        (100, 100),
        (0.5, 2),  # float + int
    ]


def test_matches_formula(rectangles):
    for length, width in rectangles:
        expected = 2 * (length + width)
        assert rectangle_perimeter(length, width) == pytest.approx(expected)


@pytest.mark.parametrize(
    "length,width,expected",
    [
        (2, 4, 12),
        (3, 5, 16),
        (10, 20, 60),
        (7, 2, 18),
        (1, 1, 4),
        (1, 5, 12),
        (4, 1, 10),
        (100, 100, 400),
        (0.5, 2, 5.0),
    ],
    ids=[
        "2x4",
        "3x5",
        "10x20",
        "7x2",
        "1x1",
        "1x5",
        "4x1",
        "100x100",
        "0.5x2",
    ],
)
def test_examples_parametrized(length, width, expected):
    assert rectangle_perimeter(length, width) == pytest.approx(expected)


@pytest.mark.parametrize(
    "length,width,expected_type",
    [
        (2, 4, int),
        (3, 5, int),
        (100, 100, int),
        (0.5, 2, float),
        (2, 0.5, float),
    ],
)
def test_return_type_depends_on_inputs(length, width, expected_type):
    result = rectangle_perimeter(length, width)
    assert isinstance(
        result, expected_type
    ), f"Expected {expected_type.__name__}, got {type(result).__name__}"
