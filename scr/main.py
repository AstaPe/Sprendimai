from scr.classes.bankaccount import BankAccount
from scr.classes.car import Car
from scr.classes.cat import Cat
from scr.classes.rectangle import Rectangle

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

# trecia uzduotis
cat1 = Cat('S')
cat2 = Cat('T')
cat3 = Cat('G')
cat4 = Cat('O')
cat5 = Cat('K')
cat6 = Cat('L')


print(f'Total number of cats: {Cat.total_cats}')

# ketvirta uzduotis
rectangle = Rectangle(10, 5)

print(f'Rectangle area: {rectangle.get_area()}')
print(f'Rectangle perimeter: {rectangle.get_perimeter()}')