from scr.classes.bankaccount import BankAccount

account = BankAccount('Asta')

account.display_balance()
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)
account.display_balance()
