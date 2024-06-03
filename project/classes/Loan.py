class Loan:
    def __init__(self, loan_amount, interest_rate, term, pledge):
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate
        self.term = term
        self.pledge = pledge
        self.monthly_payment = self.calculate_monthly_payment()

    def calculate_monthly_payment(self):
        rate = self.interest_rate / 100 / 12
        n = self.term * 12
        payment = self.loan_amount * rate / (1 - (1 + rate) ** -n)
        return payment

    def display_loan_details(self):
        return (f"Loan Amount: {self.loan_amount}, Interest Rate: {self.interest_rate}, "
                f"Term: {self.term} years, Monthly Payment: {self.monthly_payment:.2f}, "
                f"Pledge: {self.pledge.display_pledge()}")
