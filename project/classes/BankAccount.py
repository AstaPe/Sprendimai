from project.classes.Loan import Loan


class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0
        self.loans = []

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        return f"Balance: {self.balance:.2f}"

    def apply_for_loan(self, loan_amount, interest_rate, term, pledge):
        loan = Loan(loan_amount, interest_rate, term, pledge)
        self.loans.append(loan)
        return loan

    def display_loans(self):
        return [loan.display_loan_details() for loan in self.loans]
