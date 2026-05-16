from bank_account import BankAccount
from utils import get_valid_amount, display_menu


def main():
    print("\n🏦 Welcome to the Banking System!")
    name = input("Enter your name to create an account: ").strip()

    if not name:
        name = "Customer"

    account = BankAccount(account_holder=name)
    print(f"\n✅ Account created for {name}!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            amount = get_valid_amount("Enter deposit amount: $")
            account.deposit(amount)

        elif choice == "2":
            amount = get_valid_amount("Enter withdrawal amount: $")
            account.withdraw(amount)

        elif choice == "3":
            account.check_balance()

        elif choice == "4":
            account.show_transactions()

        elif choice == "5":
            print(f"\n👋 Thank you for banking with us, {name}!")
            print("   Goodbye!\n")
            break

        else:
            print("⚠️  Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
