def get_valid_amount(prompt: str) -> float:
    """Get a valid numeric amount from user."""
    while True:
        try:
            amount = float(input(prompt))
            return amount
        except ValueError:
            print("⚠️  Please enter a valid number.")


def display_menu():
    """Display the main menu options."""
    print("\n" + "=" * 40)
    print("       🏦 BANKING MANAGEMENT SYSTEM")
    print("=" * 40)
    print("  1. Deposit Money")
    print("  2. Withdraw Money")
    print("  3. Check Balance")
    print("  4. View Transaction History")
    print("  5. Exit")
    print("=" * 40)
