#!/usr/bin/env python3


def garden_operations(nb):
    """Demonstrates different error types"""

    if nb == 1:
        print("Testing ValueError...")
        int("abc")

    elif nb == 2:
        print("Testing ZeroDivisionError...")
        print(10/0)

    elif nb == 3:
        print("Testing FileNotFoundError...")
        open("missing.txt")

    elif nb == 4:
        print("Testing KeyError...")
        plant = {}
        print(plant["missing_plant"])

    else:
        print("Testing multiple errors together...")
        int("abc")
        print(10/0)
        open("missing.txt")
        garden = {}
        print(garden["missing_plant"])


def test_error_types():
    """Tests and Catches different error types"""

    try:
        garden_operations(1)
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    print()

    try:
        garden_operations(2)
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    print()

    try:
        garden_operations(3)
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    print()

    try:
        garden_operations(4)
    except KeyError:
        print("Caught KeyError: 'missing_plant'")
    print()

    try:
        garden_operations(5)
    except Exception:
        print("Caught an error, but program continues!")


def main():
    """Execute the error types"""
    print("=== Garden Error Types Demo ===\n")

    test_error_types()

    print("\nAll error types tested successfully!")


main()
