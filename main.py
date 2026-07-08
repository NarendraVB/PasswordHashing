from src.hasher import hash_password, verify_password


def main():
    while True:
        print("\n===== Password Hashing Demo =====")
        print("1. Hash Password")
        print("2. Verify Password")
        print("3. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            password = input("\nEnter password: ")

            print("\nGenerating bcrypt hash...\n")

            hashed = hash_password(password)

            print("Hash:")
            print(hashed)

            print("\nHash generated successfully.")

        elif choice == "2":
          password = input("\nEnter password: ")
          stored_hash = input("Enter stored hash: ")
          if verify_password(password, stored_hash):
                print("\n✅ Password verified.")
          else:
                print("\n❌ Password incorrect.")

        elif choice == "3":
            print("\nGoodbye!")
            break 
        else:
            print("\nInvalid option. Please try again.")




if __name__ == "__main__":
    main()