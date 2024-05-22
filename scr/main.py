from scr.classes.bankaccount import BankAccount
from scr.classes.car import Car

car1 = Car('Toyota', 'Red')
car2 = Car('Honda', 'Blue')


car1.print_info()
car2.print_info()


car1.start_engine()
car2.start_engine()

# Antra uzduotis


account = BankAccount('Asta')


account.display_balance()
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)
account.display_balance()