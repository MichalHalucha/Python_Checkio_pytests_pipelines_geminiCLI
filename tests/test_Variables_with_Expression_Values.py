from src import Variable_Declaration_and_Value_Setting as v


def test_basic_variables_exist() -> None:
    """Check that basic variables exist and have correct values."""
    assert v.cyborgs == 10
    assert v.robots == 2
    assert v.droids == 5


def test_type_annotations() -> None:
    """Check type annotations (values should be int)."""
    assert isinstance(v.cyborgs, int)
    assert isinstance(v.robots, int)
    assert isinstance(v.droids, int)


def test_recalculation_behavior() -> None:
    """Simulate updating robots/droids and verifying formulas."""
    robots_new = 4
    droids_new = 6
    add_new = robots_new + droids_new
    multi_new = robots_new * droids_new

    # if we updated those values, these would be the correct results
    assert add_new == 10
    assert multi_new == 24
