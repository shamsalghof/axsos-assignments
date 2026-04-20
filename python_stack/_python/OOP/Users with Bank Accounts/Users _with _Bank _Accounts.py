first_user = User("John", "john@gmail.com")
second_user = User("Ali", "Ali@gmail.com")
third_user = User("omar", "omar@gmail.com")

first_user.deposit(100).deposit(100).deposit(100).withdraw(150).display_user_balance()

second_user.deposit(100).deposit(100).withdraw(20).withdraw(80).display_user_balance()

third_user.deposit(100).withdraw(10).withdraw(10).withdraw(10).display_user_balance()

first_user.transfer_money(third_user,30).display_user_balance()
third_user.display_user_balance()