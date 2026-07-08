from src.hasher import hash_password, verify_password
from src.benchmark import benchmark_password
from src.comparison import compare_algorithms
from src.salt_demo import demonstrate_salt

def main():
    while True:
        print("\n===== Password Hashing Demo =====")
        print("1. Hash Password")
        print("2. Verify Password")
        print("3. Benchmark Cost Factor")
        print("4. Compare SHA-256 and bcrypt")
        print("5. Demonstrate Salt Generation")
        print("6. Exit")

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
            password = input("\nEnter password for benchmarking: ")
            benchmark_password(password)


        elif choice == "4":
            password = input("\nEnter password for comparison: ")
            compare_algorithms(password)

        elif choice == "5":
            password = input("\nEnter password for salt demonstration: ")
            demonstrate_salt(password)

        elif choice == "6":
            print("\nGoodbye!")
            break 

        else:
            print("\nInvalid option. Please try again.")




if __name__ == "__main__":
    main()