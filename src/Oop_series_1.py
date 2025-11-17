class Car:
    wheels = "four"
    doors = 4


"""Gdy wywołasz my_car.wheels, Python szuka tak:
szuka wheels w my_car.__dict__
jeśli nie znajdzie → szuka w klasie Car
jeśli nie znajdzie → w klasach bazowych (object)"""


my_car = Car()
print(my_car.__dict__)
print(my_car.wheels)  # znalazł w klasie Car a nie obiekcie
print(Car.wheels)

my_car.wheels = "three"
print(my_car.__dict__)

Car.doors = 2
print(my_car.doors)
print(Car.doors)

Car.doors = 4
print(my_car.doors)
print(Car.doors)
