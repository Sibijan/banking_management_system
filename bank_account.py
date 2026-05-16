class BankAccount:
    """Represents a bank account with basic operations."""

    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        self.account_holder = account_holder
        self._balance = initial_balance
        self.transaction_history = []

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> bool:
        """Add money to the account."""
        if amount <= 0:
            print("❌ Deposit amount must be positive.")
            return False
        self._balance += amount
        self.transaction_history.append(f"Deposited: +${amount:.2f}")
        print(f"✅ Successfully deposited ${amount:.2f}")
        return True

    def withdraw(self, amount: float) -> bool:
        """Remove money from the account."""
        if amount <= 0:
            print("❌ Withdrawal amount must be positive.")
            return False
        if amount > self._balance:
            print(f"❌ Insufficient funds. Available balance: ${self._balance:.2f}")
            return False
        self._balance -= amount
        self.transaction_history.append(f"Withdrawn: -${amount:.2f}")
        print(f"✅ Successfully withdrew ${amount:.2f}")
        return True

    def check_balance(self) -> float:
        """Display and return current balance."""
        print(f"💰 Current Balance: ${self._balance:.2f}")
        return self._balance

    def show_transactions(self):
        """Display transaction history."""
        if not self.transaction_history:
            print("📋 No transactions yet.")
            return
        print("\n📋 Transaction History:")
        print("-" * 30)
        for transaction in self.transaction_history:
            print(f"  • {transaction}")
        print("-" * 30)
