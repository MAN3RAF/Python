#!/usr/bin/env python3


def water_plants(plant_list):
    """Water plants with cleanup."""
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant is None or not isinstance(plant, str):
                raise ValueError("Cannot water None - invalid plant!")

            print(f"Watering {plant}")

    except ValueError:
        print("Error: Cannot water None - invalid plant!")

    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """Test the watering system."""
    good_list = ["tomato", "lettuce", "carrots"]

    bad_list = ["tomato", None]

    print("Testing normal watering...")
    try:
        water_plants(good_list)
    except Exception:
        pass
    finally:
        print("Watering completed successfully!")

    print("")

    print("Testing with error...")
    try:
        water_plants(bad_list)
    except Exception:
        pass
    finally:
        print("\nCleanup always happens, even with errors!")


def main():
    """Execute the test watering system"""
    print("=== Garden Watering System ===\n")

    test_watering_system()


main()
