class BankAccount:
    def __init__(self, initial_balance=0.0):
        self.balance = float(initial_balance)

    def show_balance(self):
        print(f"Current balance: ${self.balance:.2f}")

    def deposit(self, amount=None):
        if amount is None:
            try:
                amount = float(input("Enter deposit amount: "))
            except ValueError:
                print("Invalid amount.")
                return
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        self.balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount=None):
        if amount is None:
            try:
                amount = float(input("Enter withdrawal amount: "))
            except ValueError:
                print("Invalid amount.")
                return
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return

        self.balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def __str__(self):
        return f"BankAccount(balance=${self.balance:.2f})"

class SavingAccount(BankAccount):
    def __init__(self, initial_balance=0.0, interest_rate=0.02):
        super().__init__(initial_balance)
        self.interest_rate = float(interest_rate)

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Applied interest ${interest:.2f} at rate {self.interest_rate*100:.2f}%. New balance: ${self.balance:.2f}")

    def __str__(self):
        return f"SavingAccount(balance=${self.balance:.2f}, interest_rate={self.interest_rate:.2f})"