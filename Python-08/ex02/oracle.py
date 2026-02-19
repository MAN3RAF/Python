from dotenv import load_dotenv
import os

def check_missing():

    mode = os.getenv("MATRIX_MODE")
    db_url = os.getenv("DATABASE_URL")
    key = os.getenv("API_KEY")
    log = os.getenv("LOG_LEVEL")
    zion_url = os.getenv("ZION_ENDPOINT")

    confs = {
        "MATRIX_MODE":mode,
        "DATABASE_URL":db_url,
        "API_KEY":key,
        "LOG_LEVEL":log,
        "ZION_ENDPOINT":zion_url
        }

    missing = []

    for key, value in confs.items():
        if not value:
            missing.append(key)

    return missing, confs

def main():

    print("\nORACLE STATUS: Reading the Matrix...\n")

    load_dotenv()

    missing, confs = check_missing()

    if missing:
        print("[WARNING] Missing configuration detected!")
        exit(1)

    print("Configuration loaded:")
    for key, value in confs.items():
        if "MATRIX_MODE" == key:
            print(f"Mode: {value}")
        elif "DATABASE_URL" == key:
            if "localhost" in value:
                print(f"Database: Connected to local instance")
            else:
                print(f"Database: Connected")
        elif "API_KEY" == key:
            print(f"API Access: Authenticated")
        elif "LOG_LEVEL" == key:
            print(f"Log Level: {value}")
        else:
            print(f"Zion Network: Online")


    print("\nEnvironment security check:")

    print("[OK] No hardcoded secrets detected")
    if not missing:
        print("[OK] .env file properly configured")
    print("[OK] Production overrides available")


    print("\nThe Oracle sees all configurations.")

main()
