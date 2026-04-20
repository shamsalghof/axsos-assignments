class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        

    def deposit(self, amount):
        self.account_balance += amount
    def withdraw(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(f"user:{self.name} balance:{self.account_balance}")

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

first_user = User("John", "john@gmail.com")
second_user = User("Ali", "Ali@gmail.com")
third_user = User("omar", "omar@gmail.com")

first_user.deposit(100).deposit(100).deposit(100).withdraw(150).display_user_balance()

second_user.deposit(100).deposit(100).withdraw(20).withdraw(80).display_user_balance()

third_user.deposit(100).withdraw(10).withdraw(10).withdraw(10).display_user_balance()

first_user.transfer_money(third_user,30).display_user_balance()
third_user.display_user_balance()