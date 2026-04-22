# Import BankAccount class from another folder
class BankAccount:
    def __init__(self,int_rate=0.01,balance=0):
        self.int_rate=int_rate
        self.balance=balance
    
    def deposit(self, amount):
        self.balance+=amount
        return self

    def withdraw(self, amount):
        if self.balance>=amount:
            self.balance-=amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance-=5
        return self

    def display_account_info(self):
        print(f"balance:$ {self.balance}")
        return self

    def yield_interest(self):
        if self.balance>0:
            self.balance=self.balance+(self.balance*self.int_rate)
        return self   


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