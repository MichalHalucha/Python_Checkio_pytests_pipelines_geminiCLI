class AbstractCook:
    food_name = "Food"
    drink_name = "Drink"

    def __init__(self):
        self.food_total = 0
        self.drink_total = 0

    def add_food(self, food_amount, food_price):
        self.food_total += food_amount * food_price

    def add_drink(self, drink_amount, drink_price):
        self.drink_total += drink_amount * drink_price

    def total(self):
        total_sum = self.food_total + self.drink_total
        return f"{self.food_name}: {self.food_total}, {self.drink_name}: {self.drink_total}, Total: {total_sum}"


class JapaneseCook(AbstractCook):
    food_name = "Sushi"
    drink_name = "Tea"


class RussianCook(AbstractCook):
    food_name = "Dumplings"
    drink_name = "Compote"


class ItalianCook(AbstractCook):
    food_name = "Pizza"
    drink_name = "Juice"
