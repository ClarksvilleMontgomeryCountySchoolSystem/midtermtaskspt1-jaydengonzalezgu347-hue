balance = starting_balance
balance -= withdrawl_amount
# Subtract ATM fee
balance-= atm_fee - balance
total_montly_fees = balance % 30
# Calculate and subtract total monthly fees
balance -= total_monthly_fees - balance
# Calculate full $20 bills and remaining dollars
full_twenties = balance // total_monthly_fees
# Display results with f-strings
print(f"Account Holder: {account_holder}")
print(f"Remanining Balance: ")
print(f"Full")
print(f"Remaining Dollars")
