#!/usr/bin/env python
# coding: utf-8

# In[12]:


# Predefined data: Bank account details and ATM denominations
accounts = {
    "John": {"account_type": "Savings", "balance": 15000},
    "Sarah": {"account_type": "Current", "balance": 20000},
}

atm_cash = {
    2000: 5,  # Denomination: count of notes
    500: 4,
    200: 5
}



# ATM System Design Question
# Create a program to simulate an ATM system that efficiently handles user transactions, 
# account preferences, and dynamic suggestions if a user's request cannot be fulfilled. 
# The program should match user inputs such as withdrawal amount, account type, and availability of
# cash denominations.

# Program Requirements
# Predefined Account and ATM Cash Information
# 
# Create a predefined list of bank accounts with details such as:
# Account holder’s name
# Account type (e.g., Savings, Current)
# Balance
# Define ATM cash availability with denominations (₹100, ₹200, ₹500, ₹2000) and respective quantities.
# Match User Preferences for Withdrawal
# 
# Ask the user for input:
# Withdrawal amount
# Account type
# Check if the withdrawal amount can be fulfilled based on:
# Account balance
# Availability of cash denominations.
# Efficient Cash Dispensing Logic
# 
# Prioritize larger denominations first (e.g., ₹2000, ₹500) to minimize the number of notes.
# If a requested withdrawal cannot be fulfilled due to insufficient cash in specific denominations, dynamically suggest an alternative withdrawal amount (closest to the user’s request).
# Dynamic Suggestions
# 
# If the user’s requested withdrawal amount exceeds their account balance, suggest an amount closest to their balance.
# If the ATM does not have enough cash to fulfill the request, display a message explaining the mismatch and suggest the closest possible amount the ATM can dispense.
# Transaction Summary
# 
# Provide a summary of the transaction, including:
# Account holder’s name
# Withdrawal amount
# Notes dispensed (denominations and count)
# Updated account balance.
# Edge Cases to Handle
# 
# Insufficient balance in the user’s account.
# Limited cash availability in the ATM.
# Withdrawal amounts that cannot be fulfilled exactly due to denomination constraints.

# Example Input/Output
# Sample Input 1:
# 
# Account Type: Savings
# Withdrawal Amount: ₹7600
# Output:
# 
# Notes Dispensed:
# ₹2000 x 3
# ₹500 x 1
# ₹200 x 3
# ₹100 x 2
# Updated Balance: ₹14,400
# Transaction Successful.
# Sample Input 2 (Mismatch):
# 
# Account Type: Savings
# Withdrawal Amount: ₹10,000
# Output:
# 
# "Requested amount cannot be dispensed due to limited cash availability. Closest available amount: ₹9,600."
# Notes Dispensed:
# ₹2000 x 4
# ₹500 x 3
# ₹100 x 1
# Updated Balance: ₹5,400
# Sample Input 3 (Low Balance):
# 
# Account Type: Current
# Withdrawal Amount: ₹15,000
# Output:
# 
# "Insufficient account balance. Your current balance is ₹8,500. You can withdraw up to ₹8,500."

# In[13]:


def display_accounts():
    print("\nAvailable Accounts:")
    for name in accounts:
        print(f"- {name} ({accounts[name]['account_type']})")
    print("\n")

def check_balance(account_name, amount):
    if accounts[account_name]['balance'] >= amount:
        return True
    return False

def check_atm_cash(amount):
    total_cash = sum(denomination * count for denomination, count in atm_cash.items())
    return amount <= total_cash

def dispense_cash(amount):
    cash_dispensed = {}
    remaining_amount = amount

    # Prioritize larger denominations first
    for denomination in sorted(atm_cash.keys(), reverse=True):
        if remaining_amount >= denomination and atm_cash[denomination] > 0:
            notes_needed = remaining_amount // denomination
            notes_to_dispense = min(notes_needed, atm_cash[denomination])

            cash_dispensed[denomination] = notes_to_dispense
            remaining_amount -= notes_to_dispense * denomination
            atm_cash[denomination] -= notes_to_dispense

    if remaining_amount == 0:
        return cash_dispensed
    else:
        # Rollback ATM changes in case of failure
        for denomination, count in cash_dispensed.items():
            atm_cash[denomination] += count
        return None

def suggest_alternative(amount):
    # Suggest closest amount based on available cash
    total_cash = sum(denomination * atm_cash[denomination] for denomination in atm_cash)
    return total_cash if total_cash < amount else "Try smaller withdrawals."


# In[14]:


def main():
    print("Welcome to the ATM System\n")
    display_accounts()

    # Input user details
    account_name = input("Enter your account holder name: ")
    if account_name not in accounts:
        print("Invalid account name. Exiting...")
        return

    withdrawal_amount = int(input("Enter the withdrawal amount: ₹"))

    # Check balance
    if not check_balance(account_name, withdrawal_amount):
        print(f"Insufficient balance. Your balance is ₹{accounts[account_name]['balance']}.")
        return

    # Check ATM cash
    if not check_atm_cash(withdrawal_amount):
        print("ATM does not have enough cash. Please try a smaller amount.")
        return

    # Dispense cash
    cash_dispensed = dispense_cash(withdrawal_amount)
    if cash_dispensed:
        accounts[account_name]['balance'] -= withdrawal_amount
        print("\nTransaction Successful!")
        print("Cash Dispensed:")
        for denomination, count in cash_dispensed.items():
            print(f"₹{denomination} x {count}")
        print(f"Updated Balance: ₹{accounts[account_name]['balance']}")
    else:
        print("\nRequested amount cannot be dispensed due to limited denominations.")
        alternative = suggest_alternative(withdrawal_amount)
        print(f"Suggestion: Withdraw up to ₹{alternative}")

if __name__ == "__main__":
    main()


# In[ ]:




