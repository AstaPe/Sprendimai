from classes import BankSystem, Owner, Pledge, BankAccount

# Create bank system
bank = BankSystem()

# Create owner
owner = Owner("John Doe", "123 Main St", "555-1234")

# Create account
account = bank.create_account(owner, 1000)

# Display account balance
account.display_balance()

# Apply for a loan with a pledge
pledge = Pledge("Car", 5000)
bank.apply_for_loan("John Doe", 2000, 5, 2, pledge)

# Display loans
account.display_loans()
