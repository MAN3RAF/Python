#!/usr/bin/env python3

class Plant:
    """Simple factory-created plant with basic attributes."""
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


print("=== Plant Factory Output ===")

plant1 = Plant("Rose", 25, 30)
plant2 = Plant("Oak", 200, 365)
plant3 = Plant("Cactus", 5, 90)
plant4 = Plant("Sunflower", 80, 45)
plant5 = Plant("Fern", 15, 120)

print("\nTotal plants created: 5")
