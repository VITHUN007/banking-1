class savingaccount:           

    def __init__(self, initial_balance=0.0, interest_rate=0.01):
        super().__init__(initial_balance)
        self.interest_rate = interest_rate
        print(f"saving Account setup with rate: {self.interest_rate*100}%")

    def apply_interest(self):
        try:
            interest = self._BankAccount__balance * self.interest_rate
            self._BankAccount__balance += interest
            print("****************************")
            print(f"Interest of ${interest:.2f} applied.")
            self.show_balance()
            print("****************************")

        except AttributeError:
            print("Error: Could not access private balance attribute for interest calculation.")

    def __str__(self):
        try:
            return f"Account Status (Savings): Balance=${self._BankAccount__balance:.2f}, Rate={self.interest_rate*100}%"
        except AttributeError:
            return "Account Status (Savings): Balance unavailable due to private access."



