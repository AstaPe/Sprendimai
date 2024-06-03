class BankAccount:
    def __init__(self, owner, initial_balance=0.0):
        self.owner = owner
        self.balance = initial_balance
        self.loans = []

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def display_balance(self):
        print(f"Account Balance: {self.balance}")

    def apply_for_loan(self, loan_amount, interest_rate, term, pledge):
        loan = Loan(loan_amount, interest_rate, term, pledge)
        self.loans.append(loan)
        print("Loan applied successfully")

    def display_loans(self):
        for loan in self.loans:
            loan.display_loan_details()