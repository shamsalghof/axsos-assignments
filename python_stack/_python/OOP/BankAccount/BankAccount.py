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

account1= BankAccount(0.02,100)
account2 = BankAccount(0.05,800)

account1.deposit(500).deposit(100).deposit(200).withdraw(600).yield_interest().display_account_info()
account2.deposit(600).deposit(500).withdraw(200).withdraw(300).withdraw(50).yield_interest().display_account_info()