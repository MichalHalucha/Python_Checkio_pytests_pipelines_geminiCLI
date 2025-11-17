class Car:
    wheels = "four"
    doors = 4
    working_engine = False

    def __init__(self, brand="", model=""):
        self.brand = brand
        self.model = model

    def start_engine(self):
        self.working_engine = True
        print("Engine has started")

    def stop_engine(self):
        self.working_engine = False
        print("Engine has stopped")


my_car = Car()
some_car1 = Car("Ford", "Mustang")
some_car2 = Car(model="Camaro")
some_car1.start_engine()
some_car2.start_engine()
