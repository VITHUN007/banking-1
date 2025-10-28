import abc

class User:
    def __init__(self, name, age, gender):
        if not name.replace(' ', '').isalpha():
            raise ValueError("Username (name) must contain only alphabetic characters.")
        self._name = name

        if age < 18:
            raise ValueError("Age must be at least 18 to open a bank account.")
        self._age = age
        
        valid_genders = {'male', 'female', 'other'}
        if gender.lower() not in valid_genders:
            raise ValueError(f"Gender must be one of {valid_genders}.")
        self._gender = gender

    def display_details(self):
        print("-" * 30)
        print("PERSONAL DETAILS")
        print(f"Name: {self._name}")
        print(f"Age: {self._age}")
        print(f"Gender: {self._gender}")
        print("-" * 30)

class BankOperations(abc.ABC):
    @abc.abstractmethod
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Transaction amount must be positive.")
    
    @abc.abstractmethod
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        
    @abc.abstractmethod
    def view_balance(self):
        if self.__balance < 0:
            print(f" Warning: Account Overdrawn! Balance: ${self.__balance:.2f}")
        else:
            print(f"Updated Balance: ${self.__balance:.2f}")

class BankAccount(BankOperations): 
    _account_counter = 1000  

    def __init__(self, name, age, gender):
        self.user = User(name, age, gender) 
        self.__balance = 0
        self.__account_number = BankAccount._account_counter
        BankAccount._account_counter += 1 
        print(f"\nAccount created successfully for {name}!")
        print(f"Your Account Number is: {self.__account_number}")


    def display_details(self):
        self.user.display_details()
        print("ACCOUNT DETAILS")
        print(f"Account No: {self.__account_number}")
        print(f"Current Balance: ${self.__balance:.2f}")
        print("-" * 30)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit Successful. Amount: ${amount:.2f}")
        else:
            print("Invalid deposit amount. Must be positive.")
        self.view_balance()

    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"Withdrawal Successful. Amount: ${amount:.2f}")
            else:
                print("Withdrawal failed. Insufficient balance.")
        else:
            print("Invalid withdrawal amount. Must be positive.")
        self.view_balance()

    def view_balance(self):
        print(f"Updated Balance: ${self.__balance:.2f}")
        
    def get_account_number(self):
        return self.__account_number



