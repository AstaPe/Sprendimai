class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, owner, initial_balance=0.0):
        account = BankAccount(owner, initial_balance)
        self.accounts[owner.name] = account
        return account

    def get_account(self, owner_name):
        return self.accounts.get(owner_name)

    def display_accounts(self):
        for account in self.accounts.values():
            print(account.owner.name, account.balance)

    def apply_for_loan(self, owner_name, loan_amount, interest_rate, term, pledge):
        account = self.get_account(owner_name)
        if account:
            account.apply_for_loan(loan_amount, interest_rate, term, pledge)