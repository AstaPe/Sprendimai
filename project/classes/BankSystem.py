from project.classes.BankAccount import BankAccount
from project.classes.Owner import Owner
from project.classes.Pledge import Pledge


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, owner_name, address, phone):
        owner = Owner(owner_name, address, phone)
        account = BankAccount(owner)
        self.accounts[owner_name] = account
        return account

    def get_account(self, owner_name):
        return self.accounts.get(owner_name)

    def display_accounts(self):
        return [account.owner.display_info() for account in self.accounts.values()]

    def apply_for_loan(self, owner_name, loan_amount, interest_rate, term, pledge_description, pledge_value):
        account = self.get_account(owner_name)
        if account:
            pledge = Pledge(pledge_description, pledge_value)
            return account.apply_for_loan(loan_amount, interest_rate, term, pledge)
        else:
            return None
