import bcrypt


def demonstrate_salt(password: str):
    password_bytes = password.encode("utf-8")

    print("\n===== Salt Demonstration =====\n")

    hashes = []

    for i in range(5):
        hashed = bcrypt.hashpw(
            password_bytes,
            bcrypt.gensalt()
        ).decode()

        hashes.append(hashed)

        print(f"Hash {i + 1}:")
        print(hashed)
        print()

    if len(set(hashes)) == len(hashes):
        print("✓ All hashes are unique.")
        print("✓ bcrypt generated a new random salt each time.")
    else:
        print("Unexpected result: duplicate hashes detected.")