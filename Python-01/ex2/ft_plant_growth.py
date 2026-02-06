#!/usr/bin/env python3

class Plant:
    """Track plant growth over time including height and age."""
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        self.growth = 0

    def grow(self):
        self.height += 1
        self.age += 1
        self.growth += 1

    def weekly_growth(self):
        print(f"Growth this week: +{self.growth}cm")

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


rose = Plant("Rose", 25, 30)

print("=== Day 1 ===")
rose.get_info()

for i in range(6):
    rose.grow()

print("=== Day 7 ===")
rose.get_info()
rose.weekly_growth()
