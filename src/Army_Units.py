class Army:
    pass


class Swordsman:
    specialization = "swordsman"

    def __init__(self, type_name, name, army_type):
        self.type_name = type_name
        self.name = name
        self.army_type = army_type

    def introduce(self):
        return f"{self.type_name} {self.name}, {self.army_type} {self.specialization}"


class Lancer:
    specialization = "lancer"

    def __init__(self, type_name, name, army_type):
        self.type_name = type_name
        self.name = name
        self.army_type = army_type

    def introduce(self):
        return f"{self.type_name} {self.name}, {self.army_type} {self.specialization}"


class Archer:
    specialization = "archer"

    def __init__(self, type_name, name, army_type):
        self.type_name = type_name
        self.name = name
        self.army_type = army_type

    def introduce(self):
        return f"{self.type_name} {self.name}, {self.army_type} {self.specialization}"


class AsianArmy(Army):
    army_type = "Asian"

    def train_swordsman(self, name):
        return Swordsman("Samurai", name, self.army_type)

    def train_lancer(self, name):
        return Lancer("Ronin", name, self.army_type)

    def train_archer(self, name):
        return Archer("Shinobi", name, self.army_type)


class EuropeanArmy(Army):
    army_type = "European"

    def train_swordsman(self, name):
        return Swordsman("Knight", name, self.army_type)

    def train_lancer(self, name):
        return Lancer("Raubritter", name, self.army_type)

    def train_archer(self, name):
        return Archer("Ranger", name, self.army_type)
