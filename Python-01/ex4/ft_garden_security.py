#!/usr/bin/env python3

class SecurePlant:
    """Plant model with guarded setters to reject invalid updates."""
    def __init__(self, name):
        self.name = name
        self.height = 0
        self.age = 0
        print(f"Plant created: {self.name}")

    def set_height(self, height):
        if height >= 0:
            self.height = height
            print(f"Height updated: {self.height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age):
        if age >= 0:
            self.age = age
            print(f"Age updated: {age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")

    def get_height(self):
        return self.height

    def get_age(self):
        return self.age

    def get_info(self):
        print(f"Corrent plant: {self.name} ({self.height}cm, {self.age} days)")


print("=== Garden Security System ===")

rose = SecurePlant("Rose")
rose.set_height(25)
rose.set_age(30)

print("")

rose.set_height(-5)

print("")

rose.get_info()

'''
print(rose.get_height())
print(rose.get_age())
print(rose.get_info())
'''
