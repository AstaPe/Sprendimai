class BankAccount:
    def __init__(self, owner, balance=-10):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'{amount} deposited. New balance is {self.balance}.')

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds.')
        else:
            self.balance -= amount
            print(f'{amount} withdrawn. New balance is {self.balance}.')

    def display_balance(self):
        print(f'The balance of the account owned by {self.owner} is {self.balance}.')
