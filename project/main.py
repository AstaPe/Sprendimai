from project.classes.BankSystem import BankSystem

if __name__ == "__main__":
    bank_system = BankSystem()

    # Create accounts
    account_1 = bank_system.create_account("Alice", "123 Main St", "555-1234")
    account_2 = bank_system.create_account("Bob", "456 Elm St", "555-5678")

    # Display accounts
    print(bank_system.display_accounts())

    # Make deposits
    account_1.deposit(1000)
    account_2.deposit(500)

    # Display balances
    print(account_1.display_balance())
    print(account_2.display_balance())

    # Apply for a loan
    loan_1 = bank_system.apply_for_loan("Alice", 5000, 5, 10, "Car", 8000)
    print(loan_1.display_loan_details())

    # Display loans
    print(account_1.display_loans())
    print(account_2.display_loans())
