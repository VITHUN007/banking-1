from BankingAccount import SavingAccount, BankAccount

def main():
    account = SavingAccount(initial_balance=500.00)
    is_running = True

    while is_running:
        print("\n*********************")
        print(" Savings Account Program  ")
        print("*********************")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Apply Interest ")
        print("5.View Account Status")
        print("6.Exit")
        print("*********************")

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
            print("\n-------------------------")
            print(account)
            print("-------------------------")
        elif choice == '6':
            is_running = False
        else:
            print("*********************")
            print("That is not a valid choice")
            print("*********************")

    print("*********************")
    print("Thank you! Have a nice day!")
    print("*********************")

if __name__ == '__main__':
    main()
