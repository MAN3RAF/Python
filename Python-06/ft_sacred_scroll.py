import alchemy


def main() -> None:
    print("\n=== Sacred Scroll Mastery ===\n")

    print("Testing direct module access:")
    fire = alchemy.elements.create_fire()
    print(f"alchemy.elements.create_fire(): {fire}")
    water = alchemy.elements.create_water()
    print(f"alchemy.elements.create_water(): {water}")
    earth = alchemy.elements.create_earth()
    print(f"alchemy.elements.create_earth(): {earth}")
    air = alchemy.elements.create_air()
    print(f"alchemy.elements.create_air(): {air}")

    try:
        print("\nTesting package-level access (controlled by __init__.py):")
        print(f"alchemy.create_fire(): {alchemy.create_fire()}")
        print(f"alchemy.create_water(): {alchemy.create_water()}")
        print(f"alchemy.create_earth(): {alchemy.create_earth()}")
        print(f"alchemy.create_air(): {alchemy.create_air()}")
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed"
              "\nalchemy.create_air(): AttributeError - not exposed")

    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    main()
