import pytest

from src.Backward_String import backward_string

@pytest.mark.parametrize(
    "normal, reserved",
    [
        ("val", "lav"),
        ("", ""),
        ("ohho", "ohho"),
        ("123456789", "987654321"),
    ],
)

def test_backward_string(normal: str, reserved: str):
    assert backward_string(normal) == reserved
