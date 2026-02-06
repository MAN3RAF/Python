

def main():

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    try:
        vault_name = "ancient_fragment.txt"
        print(f"Accessing Storage Vault: {vault_name}")

        vault = open(vault_name)

        print("Connection established...\n")

        recovered_data = vault.read()

        print(f"RECOVERED DATA:\n{recovered_data}")

        vault.close()
        print("\nData recovery complete. Storage unit disconnected.")

    except FileNotFoundError:
        print("\nERROR: Storage vault cannot be accessed due to coruption!")


main()
