from alchemy.elements import create_fire, create_water
from alchemy.elements import create_earth
import alchemy.elements
from alchemy.potions import strength_potion
from alchemy.potions import healing_potion as heal

def main() -> None:
    print("\n=== Import Transmutation Mastery ===\n")

    print("Method 1 - Full module import:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")

    print("Method 2 - Specific function import:")
    print(f"create_water(): {create_water()}")

    print("Method 3 - Aliased import:")
    print(f"heal(): {heal()}")

    print("Method 4 - Multiple imports:")
    print(f"create_earth(): {create_earth()}")
    print(f"create_fire(): {create_fire()}")
    print(f"strength_potion(): {strength_potion()}")

    print("\nAll import transmutation methods mastered!")

if __name__ == "__main__":
    main()
