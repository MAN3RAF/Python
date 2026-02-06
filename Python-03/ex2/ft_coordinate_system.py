import math


def main() -> None:
    """Demonstrate 3D coordinate parsing and distance calculations."""
    position = tuple([10, 20, 5])
    spawn = tuple([0, 0, 0])

    x1, y1, z1 = position

    x2, y2, z2 = spawn

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

    print("=== Game Coordinate System ===\n")

    print(f"Position created: {position}")
    print(f"Distance between {spawn} and {position}: {distance:.2f}")

    print("")

    coords = "3,4,0"
    print(f'Parsing coordinates: "{coords}"')
    try:
        position = tuple(int(n) for n in coords.split(","))
        x1, y1, z1 = position

        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

        print(f"Parsed position: ({x1}, {y1}, {z1})")
        print(
            f"Distance between ({x2}, {y2}, {z2}) "
            f"and ({x1}, {y1}, {z1}): {distance}"
        )

    except ValueError as e:
        print("Error parsing coordinates:", e)
        print(f'Error details - Type: ValueError, Args: ("{e}",)')

    print("")

    coords = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{coords}"')
    try:
        position = tuple(int(n) for n in coords.split(","))

        x1, y1, z1 = position

        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

        print(f"Parsed position: ({position})")
        print(
            f"Distance between ({x2}, {y2}, {z2}) "
            f"and ({position}): {distance}"
        )

    except ValueError as e:
        print("Error parsing coordinates:", e)
        print(f'Error details - Type: ValueError, Args: ("{e}",)')

    print("")

    print("Unpacking demonstration:")
    print(f"Player at x={x1}, y={y1}, z={z1}")
    print(f"Coordinates: X={x1}, Y={y1}, Z={z1}")


main()
