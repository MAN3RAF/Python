#!/usr/bin/env python3

class Plant:
    """Base plant type shared by flowers, trees, and vegetables."""
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """Flower that can bloom and carries a color attribute."""
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """Tree with trunk diameter that can compute provided shade."""
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade = self.trunk_diameter * 1.56
        print(f"{self.name} provides {int(shade)} square meters of shade")


class Vegetable(Plant):
    """Vegetable tracking harvest season and nutritional value."""
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def vitamin(self):
        print(f"{self.name} is rich in {self.nutritional_value}")


print("=== Garden Plant Types ===")

print("")

rose = Flower("rose", 25, 30, "red")
tulip = Flower("tulip", 15, 25, "yellow")
print(
    f"{rose.name} (Flower): {rose.height}cm, "
    f"{rose.age} days, {rose.color} color"
)
rose.bloom()

print("")

oak = Tree("Oak", 500, 1825, 50)
birch = Tree("Birch", 400, 1545, 35)
print(
    f"{oak.name} (Tree): {oak.height}cm, "
    f"{oak.age} days, {oak.trunk_diameter}cm diameter"
)
oak.produce_shade()

print("")

tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
potato = Vegetable("Potato", 30, 70, "spring", "vitamin A")
print(
    f"{tomato.name} (Vegetable): {tomato.height}cm, "
    f"{tomato.age} days, {tomato.harvest_season} harvest"
)
tomato.vitamin()
