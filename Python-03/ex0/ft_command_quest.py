import sys


def main() -> None:
    """Process and display command line arguments."""
    program_name = sys.argv[0]
    program_len = len(sys.argv)

    print("=== Command Quest ===")

    if program_len < 2:
        print("No arguments provided!")
        print(f"Program name: {program_name}")
        print(f"Total arguments: {program_len}")
    else:
        print(f"Program name: {program_name}")
        print(f"Arguments received: {program_len - 1}")
        for i in range(1, len(sys.argv)):
            print(f"Argument {i}: {sys.argv[i]}")
        print(f"Total arguments: {program_len}")


main()
