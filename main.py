from BankingAccount import BankAccount, SavingAccount

def main():
    account = SavingAccount(initial_balance=500.00, interest_rate=0.05)
    print("Welcome! New account initialized.")
    is_running = True

    while is_running:
        print("\n" + "="*30)
        print(" Savings Account Menu ")
        print("="*30)
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Apply Interest")
        print("5. View Account Status")
        print("6. Exit")
        print("="*30)

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            account.show_balance()
        elif choice == '2':
            account.deposit()
        elif choice == '3':
            account.withdraw()
        elif choice == '4':
            account.apply_interest()
        elif choice == '5':
            print("\n" + "-"*30)
            print(account) 
            print("-"*30)
        elif choice == '6':
            is_running = False
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")

    print("\n" + "="*30)
    print("Thank you! Have a nice day!")
    print("="*30)

if __name__ == '__main__':
    main()