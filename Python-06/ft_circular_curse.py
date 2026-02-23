from alchemy.grimoire.validator import validate_ingredients as validate
from alchemy.grimoire import record_spell


def main() -> None:
    print("\n=== Circular Curse Breaking ===\n")

    print("Testing ingredient validation:")
    result1 = validate("fire air")
    print(f'validate_ingredients("fire air"): {result1}')
    result2 = validate("dragon scales")
    print(f'validate_ingredients("dragon scales"): {result2}')

    print("\nTesting spell recording with validation:")
    print('record_spell("Fireball", "fire air"): '
          f'{record_spell("Fireball", "fire air")}')
    print('record_spell("Dark Magic", "shadow"): '
          f'{record_spell("Dark Magic", "shadow")}')

    print("\nTesting late import technique:")
    print('record_spell("Lightning", "air"): '
          f'{record_spell("Lightning", "air")}')

    print("\nCircular dependency curse avoided using late imports!\n"
          "All spells processed safely!")


if __name__ == "__main__":
    main()
