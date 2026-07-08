from src.hasher import hash_password


def main():
    while True:
        print("\n===== Password Hashing Demo =====")
        print("1. Hash Password")
        print("2. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            password = input("\nEnter password: ")

            print("\nGenerating bcrypt hash...\n")

            hashed = hash_password(password)

            print("Hash:")
            print(hashed)

            print("\nHash generated successfully.")

        elif choice == "2":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid option.")


if __name__ == "__main__":
    main()