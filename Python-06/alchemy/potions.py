from .elements import create_fire, create_water
from alchemy.elements import create_earth
import alchemy.elements

def healing_potion() -> str:
    return f"Healing potion brewed with {create_fire()} and {create_water()}"

def strength_potion() -> str:
    return f"Strength potion brewed with {create_earth()} and {create_fire()}"

def invisibility_potion() -> str:
    return (f"Invisibility potion brewed with {alchemy.elements.create_air()}"
            f" and {create_water()}")

def wisdom_potion() -> str:
    return ("Wisdom potion brewed with all elements: "
            f"{alchemy.elements.create_air()} {create_water()} "
            f"{create_earth()} {create_fire()}")
