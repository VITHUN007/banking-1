## A simple Bank Management System built using Object-Oriented Programming (OOP) principles in Python.
The project demonstrates Encapsulation, Inheritance, Polymorphism, and Abstraction — implemented with separate class files for modular design.
### bankproject Structure

bankaccount.py

savingaccount.py

main.py 

 README.md 

### CONCEPT USED
OOP Concept used

* Encapsulation Hiding data using private attributes

* Inheritance Reusing the base class savingaccount

* Polymorphism single action different ways(display_account) used in both class es 

* Abstraction User interacts through a menu, not inner details (main.py)

### FEATURES
1. Create a savings account
2. Deposit and withdraw money
3. View account details
4. Check current balance
5. Add interest automatically-- Fully encapsulated and modular design

### Installation & Setup
Clone or Download this project folder:
git clone : https://github.com/VITHUN007/banking.git

Ensure Python is installed:
python --version

SAMPLE OUTPUT
Account created with initial balance: $500.00 Savings Account setup with rate: 2.0%
Savings Account Program

1. Show Balance
2. Deposit
3. withdraw
 4. Apply Interest
5. View Account Status
6. Exit

Enter your choice (1-6): 1

Your balance is $500.00

Savings Account Program

1.Show Balance 2.Deposit 3.Withdraw 4.Apply Interest 5.View Account Status 6.Exit

Enter your choice (1-6): 4

Interest of $5.00 applied.

Your balance is $505.00

Savings Account Program

1.Show Balance 2.Deposit 3.Withdraw 4.Apply Interest 5.View Account Status 6.Exit

Enter your choice (1-6): 2

Enter an amount to be deposited: 45 Deposit of $45.00 successful.

Savings Account Program

1.Show Balance 2.Deposit 3.Withdraw 4.Apply Interest 5.View Account Status 6.Exit

Enter your choice (1-6): 1

Your balance is $550.00

### Class Overview
BankAccount :

Attributes: account_number, __name, __balance

Methods:deposit(amount),withdraw(amount)
get_balance(), set_balance(amount)
get_name(), set_name(name)
display_account()

SavingsAccounT (inherits from BankAccount) :

Additional Attribute: interest_rate
Additional Methods:
add_interest() ,Overridden display_account()

### Learning Outcome
By studying and running this project, you’ll understand how:

OOP concepts work together in Python

Private, protected, and public access modifiers function

To organize a Python project using multiple modules

Real-world problems can be modeled using classes and inheritance

