import sys

from BankingAccount import User, BankAccount

if __name__ == "__main__":
    accounts = {}
    
    def get_valid_input(prompt, input_type=str):
        while True:
            try:
                if input_type == int:
                    value = int(input(prompt))
                    if value < 0:
                        raise ValueError("Value cannot be negative.")
                elif input_type == float:
                    value = float(input(prompt))
                    if value < 0:
                        raise ValueError("Value cannot be negative.")
                else:
                    value = input(prompt).strip()
                    if not value:
                        raise ValueError("Input cannot be empty.")
                return value
            except ValueError as e:
                print(f"Error: {e}. Please try again.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}. Please try again.")

    def create_account_flow():
        print("\n--- NEW ACCOUNT REGISTRATION ---")
        name = get_valid_input("Enter account holder's name: ")
        age = get_valid_input("Enter age: ", int)
        gender = get_valid_input("Enter gender: ")
        
        try:
            new_account = BankAccount(name, age, gender) 
            accounts[new_account.get_account_number()] = new_account
        except Exception as e:
            print(f"Could not create account: {e}")

    def transaction_flow(action):
        print(f"\n--- {action.upper()} TRANSACTION ---")
        acc_num = get_valid_input("Enter your Account Number: ", int)
        
        if acc_num not in accounts:
            print("Error: Account Number not found.")
            return

        account = accounts[acc_num]
        
        try:
            amount = get_valid_input(f"Enter amount to {action}: $", float)
            if action == "deposit":
                account.deposit(amount)
            elif action == "withdraw":
                account.withdraw(amount)
        except Exception:
            print("Transaction failed. Please ensure the amount is a valid number.")

    print("\n" + "=" * 40)
    print("WELCOME TO THE OOP BANK MANAGEMENT SYSTEM")
    print("=" * 40)

    while True:
        print("\nWhat would you like to do?")
        print("1. Create New Account")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. View Account Details & Balance")
        print("5. Exit System")
        
        choice = get_valid_input("Enter choice (1-5): ", int)

        if choice == 1:
            create_account_flow()
        elif choice == 2:
            transaction_flow("deposit")
        elif choice == 3:
            transaction_flow("withdraw")
        elif choice == 4:
            print("\n--- ACCOUNT DETAILS QUERY ---")
            acc_num = get_valid_input("Enter your Account Number: ", int)
            if acc_num in accounts:
                accounts[acc_num].display_details()
            else:
                print("Error: Account Number not found.")
        elif choice == 5:
            print("\nThank you. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
