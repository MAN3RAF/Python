#!/usr/bin/env python3


def check_temperature(temp_str):
    """Check if temperature is safe for plants."""
    try:
        print(f"Testing temperature: {temp_str}")
        temperature = int(temp_str)

        if temperature < 0:
            print(f"Error: {temperature}°C is too cold for plants (min 0°C)")
            return None

        elif temperature > 40:
            print(f"Error: {temperature}°C is too hot for plants (max 40°C)")
            return None

        else:
            return temperature

    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None


def test_temperature_input():
    print("=== Garden Temperature Checker ===\n")

    print(f"Temperature {check_temperature("25")}°C is perfect for plants!")
    print("")

    check_temperature("abc")
    print("")

    check_temperature("100")
    print("")

    check_temperature("-50")
    print("")

    print("All tests completed - program didn't crash!")


test_temperature_input()
