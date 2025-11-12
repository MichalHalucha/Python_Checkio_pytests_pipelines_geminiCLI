import pytest
from src.Take_And_Return_Argument import func   # ⬅️ zmień 'example' na nazwę swojego modułu, np. 'Empty_Function'

def test_func_returns_same_value_for_int():
    assert func(42) == 42

def test_func_returns_same_value_for_string():
    assert func("hello") == "hello"

def test_func_returns_same_value_for_list():
    data = [1, 2, 3]
    result = func(data)
    # wartość powinna być taka sama
    assert result == data
    # i to ten sam obiekt (bo nic nie jest kopiowane)
    assert result is data

def test_func_returns_same_value_for_dict():
    d = {"a": 1}
    assert func(d) == d
    assert func(d) is d

def test_func_works_with_none():
    assert func(None) is None

@pytest.mark.parametrize("value", [0, "abc", [1], {"k": 9}, (1, 2)])
def test_func_parametrized(value):
    assert func(value) == value
