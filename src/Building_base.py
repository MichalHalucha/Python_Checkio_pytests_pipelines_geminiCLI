class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south = south
        self.west = west
        self.width_WE = width_WE
        self.width_NS = width_NS
        self.height = height

    def corners(self):
        north = self.south + self.width_NS
        east = self.west + self.width_WE
        return {
            "south-west": [self.south, self.west],
            "south-east": [self.south, east],
            "north-west": [north, self.west],
            "north-east": [north, east],
        }

    def area(self):
        return self.width_WE * self.width_NS

    def volume(self):
        return self.area() * self.height

    def __repr__(self):
        return f"Building({self.south}, {self.west}, {self.width_WE}, {self.width_NS}, {self.height})"
