

def main():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    try:
        print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")

        with open("lost_archive.txt", "r") as lost_archive:
            lost_archive.read()
            print(
                "SUCCESS: Archive recovered - "
                "``Knowledge preserved for humanity''")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    try:
        print("\nCRISIS ALERT: Attempting access to 'classified_vault.txt'...")

        with open("classified_vault.txt", "r"):
            pass

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    try:
        print(
            "\nROUTINE ACCESS: Attempting access to "
            "'standard_archive.txt'...")

        with open("standard_archive.txt", "r") as standard_archive:

            recovered_data = standard_archive.readline()

            print(
                f"SUCCESS: Archive recovered - ``{recovered_data}''")

            print("STATUS: Normal operations resumed")

    except Exception:
        print("STATUS: Could not get standard_archive")

    print("\nAll crisis scenarios handled successfully. Archives secure.")


main()
