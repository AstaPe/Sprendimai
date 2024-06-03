from project.classes.BankSystem import BankSystem, BankAccount

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

    # Display accounts
    print("Accounts in the system:")
    for account_info in bank_system.display_accounts():
        print(account_info)

    # Make deposits
    account_1.deposit(0)
    account_2.deposit(0)

    account_1.withdraw(1000000)
    account_2.withdraw(3500000)

    # Display balances
    print(f"Balance for Alice: {account_1.display_balance()}")
    print(f"Balance for Bob: {account_2.display_balance()}")

    # Apply for a loan
    loan_1 = bank_system.apply_for_loan("Alice", 5000, 5, 10, "Car", 8000)
    if loan_1:
        print("Loan details for Alice:")
        print(loan_1.display_loan_details())
    else:
        print("Failed to apply for loan for Alice")

    # Apply for another loan
    loan_2 = bank_system.apply_for_loan("Bob", 3000, 4.5, 5, "Bike", 2000)
    if loan_2:
        print("Loan details for Bob:")
        print(loan_2.display_loan_details())
    else:
        print("Failed to apply for loan for Bob")

    # Display loans for Alice
    print("All loans for Alice:")
    for loan_details in account_1.display_loans():
        print(loan_details)

    # Display loans for Bob
    print("All loans for Bob:")
    for loan_details in account_2.display_loans():
        print(loan_details)

    account_1.withdraw(10000)
    account_2.withdraw(20000)

    # Display balances
    print(f"Balance for Alice: {account_1.display_balance()}")
    print(f"Balance for Bob: {account_2.display_balance()}")


