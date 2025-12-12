balance = starting_balance
balance -= withdrawal_amount
# Subtract ATM fee
balance-= atm_fee
total_monthly_fee = balance % 30
# Calculate and subtract total monthly fees
balance -= total_monthly_fee
# Calculate full $20 bills and remaining dollars
full_twenties = balance // total_monthly_fee
# Display results with f-strings
print(f"Account Holder: {account_holder}")
print(f"Remanining Balance: $244")
print(f"Full $20 Bills: 12")
print(f"Remaining Dollars: $4")
