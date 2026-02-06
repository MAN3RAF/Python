import sys


def main():
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    archivist_ID = input("Input Stream active. Enter archivist ID: ")

    print("Input Stream active. Enter status report:", end=' ')

    sys.stdout.flush()

    status_report = sys.stdin.readline()

    sys.stdout.write(
        f"\n[STANDARD] Archive status from {archivist_ID}: "
        f"{status_report}")

    sys.stderr.write(
        "[ALERT] System diagnostic: Communication channels verified\n")

    sys.stdout.write("[STANDARD] Data transmission complete\n")

    print("\nThree-channel communication test successful.")


main()
