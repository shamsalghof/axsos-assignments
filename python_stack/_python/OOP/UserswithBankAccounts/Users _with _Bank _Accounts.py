# Import BankAccount class from another folder
from BankAccount.BankAccount import BankAccount 


class User:
    def __init__(self, name, email_address):
        # Store user name
        self.name = name
        
        # Store user email
        self.email = email_address
        
        # Each user has one bank account
        self.account = BankAccount(int_rate=0.02, balance=0)


    # Deposit money into user's bank account
    def deposit(self, amount):
        self.account.deposit(amount)   # call BankAccount deposit method
        return self                    # return self for method chaining


    # Withdraw money from user's bank account
    def withdraw(self, amount):
        self.account.withdraw(amount)
        return self


    # Display user balance
    def display_user_balance(self):
        print(f"user:{self.name} balance:{self.account.balance}")
        return self


    # Transfer money from one user to another
    def transfer_money(self, other_user, amount):
        self.account.withdraw(amount)         # withdraw from current user
        other_user.account.deposit(amount)    # deposit to other user
        return self


# Create Users
first_user = User("John", "john@gmail.com")
second_user = User("Ali", "Ali@gmail.com")
third_user = User("omar", "omar@gmail.com")


# Method chaining operations
first_user.deposit(100).deposit(100).deposit(100).withdraw(150).display_user_balance()

second_user.deposit(100).deposit(100).withdraw(20).withdraw(80).display_user_balance()

third_user.deposit(100).withdraw(10).withdraw(10).withdraw(10).display_user_balance()

# Transfer money between users
first_user.transfer_money(third_user,30).display_user_balance()
third_user.display_user_balance()