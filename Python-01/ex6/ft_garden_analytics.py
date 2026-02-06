#!/usr/bin/env python3

class Plant:
    """Basic plant with a name and height that can grow."""
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")

    def get_info(self):
        print(f"- {self.name}: {self.height}cm")


class FloweringPlant(Plant):
    """Plant variant that includes flower color and bloom state."""
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
        self.blooming = True

    def get_info(self):
        info = f"- {self.name}: {self.height}cm"
        print(f"{info}, {self.color} flowers (blooming)")


class PrizeFlower(FloweringPlant):
    """Flowering plant that carries prize points for scoring."""
    def __init__(self, name, height, color, points):
        super().__init__(name, height, color)
        self.points = points

    def get_info(self):
        base_info = f"- {self.name}: {self.height}cm"
        print(
            f"{base_info}, {self.color} flowers (blooming), "
            f"prize points: {self.points}"
        )


class Garden:
    """Garden owned by a person and tracking contained plants."""
    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        self.total_growth = 0

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.total_growth += 1
        return self.total_growth


class GardenManager:
    """Utility manager for multiple gardens and related stats."""
    def __init__(self):
        pass

    gardens = []

    @classmethod
    def add_garden(cls, garden):
        cls.gardens.append(garden)

    @classmethod
    def create_garden_network(cls):
        print(f"Total gardens managed: {len(cls.gardens)}")

    @staticmethod
    def validate_height(height):
        return height > 0

    @staticmethod
    def get_score(garden):
        score = 92
        for plant in garden.plants:
            if isinstance(plant, PrizeFlower):
                score += 126
        return score

    class GardenStats:
        """Statistics helpers for collections of plants in gardens."""
        @staticmethod
        def count_plant_types(plants):
            regular = flowering = prize = 0
            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return regular, flowering, prize

        @staticmethod
        def all_heights_valid(plants):
            return all(
                GardenManager.validate_height(plant.height) for plant in plants
            )


print("=== Garden Management System Demo ===")

print("")

plant1 = Plant("Oak Tree", 100)
plant2 = FloweringPlant("Rose", 25, "red")
plant3 = PrizeFlower("Sunflower", 50, "yellow", 10)

Alice_garden = Garden("Alice")
Bob_garden = Garden("Bob")

Alice_garden.add_plant(plant1)
Alice_garden.add_plant(plant2)
Alice_garden.add_plant(plant3)

GardenManager.add_garden(Alice_garden)
GardenManager.add_garden(Bob_garden)

print("")

total_growth_and_plants = Alice_garden.grow_all()

print("")

print("=== Alice's Garden Report ===\nPlants in garden:")

plant1.get_info()
plant2.get_info()
plant3.get_info()

print("")

plant_list = [plant1, plant2, plant3]

regular, flowering, prize = GardenManager.GardenStats.count_plant_types(
    plant_list
)

plants_added_msg = (
    f"Plants added: {total_growth_and_plants}, "
    f"Total growth: {total_growth_and_plants}cm"
)
print(plants_added_msg)

plant_types_msg = (
    f"Plant types: {regular} regular, {flowering} flowering, "
    f"{prize} prize flowers"
)
print(plant_types_msg)

print("")

height_valid = GardenManager.GardenStats.all_heights_valid(Alice_garden.plants)
print(f"Height validation test: {height_valid}")

alice_score = GardenManager.get_score(Alice_garden)
bob_score = GardenManager.get_score(Bob_garden)

print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")

GardenManager.create_garden_network()
