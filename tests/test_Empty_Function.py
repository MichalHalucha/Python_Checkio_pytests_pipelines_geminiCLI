import inspect

from src import Empty_Function as Ef
from src.Empty_Function import func


def test_if_ef_is_empty() -> None:
    source = inspect.getsource(Ef).strip()
    assert source in ("def func():\n    pass", "def func(): pass")


def test_func_returns_none_and_does_nothing() -> None:
    assert func() is None

