
import time
import getpass
import hashlib
import hmac

MAX_ATTEMPTS = 3
LOCK_TIME = 30

USERNAME = "admin"
PASSWORD_HASH = hashlib.sha256(
    b"Admin@123"
).digest()

failed_attempts = 0
locked_until = 0


def verify_password(password):
    entered_hash = hashlib.sha256(
        password.encode("utf-8")
    ).digest()

    return hmac.compare_digest(
        entered_hash, PASSWORD_HASH
    )


def login():
    global failed_attempts, locked_until

    remaining = locked_until - time.monotonic()

    if remaining > 0:
        print(f"[LOCKED] Try again in {remaining:.0f} seconds.")
        return

    if locked_until > 0:
        failed_attempts = 0
        locked_until = 0

    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    if username == USERNAME and verify_password(password):
        print("[SUCCESS] Login successful!")
        failed_attempts = 0
    else:
        failed_attempts += 1
        print("[FAILED] Invalid username or password.")

        if failed_attempts >= MAX_ATTEMPTS:
            locked_until = time.monotonic() + LOCK_TIME
            print("[LOCKED] Too many failed attempts.")
            print("Account locked for 30 seconds.")


def main():
    while True:
        print("\n================================")
        print("    LOGIN ATTEMPT CONTROL SYSTEM")
        print("================================")
        print("1. Login")
        print("2. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            login()
        elif choice == "2":
            print("Thank you!")
            break
        else:
            print("[ERROR] Invalid choice.")


if __name__ == "__main__":
    main()
