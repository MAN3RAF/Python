#!/usr/bin/env python3


def check_plant_health(plant_name, water_level, sunlight_hours):
    if not plant_name:
        raise ValueError("Error: Plant name cannot be empty!")

    if water_level > 10:
        raise ValueError(
            f"Error: Water level {water_level} is too high (max 10)"
            )
    if water_level < 1:
        raise ValueError(
            f"Error: Water level {water_level} is too low (min 1)"
            )

    if sunlight_hours < 2:
        raise ValueError(
            f"Error: Sunlight hours {sunlight_hours} is too low (min 2)"
            )
    if sunlight_hours > 12:
        raise ValueError(
            f"Error: Sunlight hours {sunlight_hours} is too high (max 12)"
            )

    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks():
    """Test the plant health checker."""

    print("Testing good values...")
    try:
        print(check_plant_health("tomato", 5, 5))
    except ValueError as e:
        print(e)

    print("")

    print("Testing empty plant name...")
    try:
        check_plant_health("", 5, 5)
    except ValueError as e:
        print(e)

    print("")

    print("Testing bad water level...")
    try:
        check_plant_health("tomato", 15, 5)
    except ValueError as e:
        print(e)

    print("")

    print("Testing bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(e)


def main():
    """a main function for testing"""
    print("=== Garden Plant Health Checker ===")

    print("")

    test_plant_checks()

    print("")

    print("All error raising tests completed!")


main()
