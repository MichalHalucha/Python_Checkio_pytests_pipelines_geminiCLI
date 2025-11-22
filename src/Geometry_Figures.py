import math


class Parameters:
    def __init__(self, size):
        # size = promień / bok / krawędź – zależnie od figury
        self.size = size
        self._figure = None

    def choose_figure(self, figure):
        # figure to strategia, np. Circle(), Square(), Cube()...
        self._figure = figure

    def _format(self, value):
        # jeśli wynik jest "całkowity" → int
        # inaczej → zaokrąglij do 2 miejsc po przecinku
        if isinstance(value, int):
            return value
        if isinstance(value, float) and value.is_integer():
            return int(value)
        return round(value, 2)

    def perimeter(self):
        result = self._figure.perimeter(self.size)
        return self._format(result)

    def area(self):
        result = self._figure.area(self.size)
        return self._format(result)

    def volume(self):
        result = self._figure.volume(self.size)
        return self._format(result)


class Circle:
    # size = promień
    def perimeter(self, r):
        return 2 * math.pi * r

    def area(self, r):
        return math.pi * r * r

    def volume(self, r):
        return 0


class Triangle:
    # równoboczny, size = bok
    def perimeter(self, a):
        return 3 * a

    def area(self, a):
        return (math.sqrt(3) / 4) * a * a

    def volume(self, a):
        return 0


class Square:
    # size = bok
    def perimeter(self, a):
        return 4 * a

    def area(self, a):
        return a * a

    def volume(self, a):
        return 0


class Pentagon:
    # foremny pięciokąt, size = bok
    def perimeter(self, a):
        return 5 * a

    def area(self, a):
        return 1 / 4 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * a * a

    def volume(self, a):
        return 0


class Hexagon:
    # foremny sześciokąt, size = bok
    def perimeter(self, a):
        return 6 * a

    def area(self, a):
        return (3 * math.sqrt(3) / 2) * a * a

    def volume(self, a):
        return 0


class Cube:
    # sześcian, size = krawędź
    def perimeter(self, a):
        # przyjmijmy sumę długości wszystkich krawędzi
        return 12 * a

    def area(self, a):
        return 6 * a * a

    def volume(self, a):
        return a**3
