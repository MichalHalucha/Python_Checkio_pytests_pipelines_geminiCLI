# tests/conftest.py
import pytest

from src.Oop_series_4 import Car


@pytest.fixture
def car():
    return Car()


@pytest.fixture
def ford_mustang():
    return Car("Ford", "Mustang")


@pytest.fixture
def camaro():
    return Car(model="Camaro")


# tests/test_car.py
def test_class_attributes_exist_and_values():
    # atrybuty klasowe
    assert Car.wheels == "four"
    assert Car.doors == 4
    assert Car.working_engine is False


def test_default_init_values(car):
    # domyślne wartości konstruktora
    assert car.brand == ""
    assert car.model == ""
    # working_engine startowo False
    assert car.working_engine is False


@pytest.mark.parametrize(
    "brand, model",
    [
        ("Ford", "Mustang"),
        ("Toyota", "Corolla"),
        ("", "Camaro"),
        ("BMW", ""),
    ],
)
def test_init_with_parameters(brand, model):
    c = Car(brand=brand, model=model)
    assert c.brand == brand
    assert c.model == model


def test_start_engine_sets_flag_and_prints(capsys, car):
    assert car.working_engine is False

    car.start_engine()

    assert car.working_engine is True

    captured = capsys.readouterr()
    assert "Engine has started" in captured.out


def test_stop_engine_sets_flag_and_prints(capsys, car):
    # najpierw odpalamy silnik
    car.start_engine()
    assert car.working_engine is True

    car.stop_engine()

    # flaga wraca na False
    assert car.working_engine is False

    captured = capsys.readouterr()
    assert "Engine has stopped" in captured.out


def test_engine_state_independent_between_instances():
    c1 = Car()
    c2 = Car()

    assert c1.working_engine is False
    assert c2.working_engine is False

    c1.start_engine()
    assert c1.working_engine is True
    assert c2.working_engine is False

    c2.start_engine()
    assert c2.working_engine is True


def test_brand_and_model_with_fixtures(ford_mustang, camaro):
    # ford_mustang fixture
    assert ford_mustang.brand == "Ford"
    assert ford_mustang.model == "Mustang"

    assert camaro.brand == ""
    assert camaro.model == "Camaro"
