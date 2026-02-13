import alchemy

def main() -> None:
    print("=== Sacred Scroll Mastery ===\n")

    print("Testing direct module access:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    print(f"alchemy.elements.create_water(): {alchemy.elements.create_water()}")
    print(f"alchemy.elements.create_earth(): {alchemy.elements.create_earth()}")
    print(f"alchemy.elements.create_air(): {alchemy.elements.create_air()}")

    try:
        print("\nTesting package-level access (controlled by __init__.py):")
        print(f"alchemy.elements.create_fire(): {alchemy.create_fire()}")
        print(f"alchemy.elements.create_water(): {alchemy.create_water()}")
        print(f"alchemy.elements.create_earth(): {alchemy.create_earth()}")
        print(f"alchemy.elements.create_air(): {alchemy.create_air()}")
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed"
              "\nalchemy.create_air(): AttributeError - not exposed")

    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")

if __name__ == "__main__":
    main()
