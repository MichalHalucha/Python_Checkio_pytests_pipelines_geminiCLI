import pytest

from src.Oop_series_1 import Car, my_car


@pytest.fixture
def car():
    return Car()


@pytest.fixture
def shared_car():
    return my_car


@pytest.mark.parametrize("obj", [Car(), Car(), Car()])
def test_default_class_attributes(obj):
    assert obj.wheels == "four"
    assert obj.doors == 4


@pytest.mark.parametrize("factory", ["car", "shared_car"])
def test_fixtures_provide_car_instances(request, factory):
    obj = request.getfixturevalue(factory)
    assert isinstance(obj, Car)


def test_class_and_instance_attribute_behavior():
    c1 = Car()
    c2 = Car()

    assert c1.wheels == "four"
    assert c2.wheels == "four"

    c1.wheels = "three"

    assert c1.wheels == "three"  # instance override
    assert c2.wheels == "four"  # still class value
    assert Car.wheels == "four"
