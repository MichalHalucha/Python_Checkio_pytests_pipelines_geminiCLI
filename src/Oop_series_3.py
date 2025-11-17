class Car:
    wheels = "four"
    doors = 4

    def __init__(self, brand="", model=""):
        self.brand = brand
        self.model = model


my_car = Car()
some_car1 = Car("Ford", "Mustang")
some_car2 = Car(model="Camaro")
