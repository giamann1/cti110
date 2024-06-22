# Gia Manning
# 06-21-2024
# P1HW2
# This program helps the user plan their travel budget by asking for their total budget, travel destination, and expenses on gas, accommodation, and food. It then calculates the remaining budget after expenses.

# Step 3: Ask user to enter their budget
budget = float(input("Enter your budget for the trip: "))

# Step 4: Ask user to enter travel destination
destination = input("Enter your travel destination: ")

# Step 5: Ask user for amount they will spend on gas
gas_expense = float(input("Enter the amount you will spend on gas: "))

# Step 6: Ask user for amount they will spend on accommodation
accommodation_expense = float(input("Enter the amount you will spend on accommodation: "))

# Step 7: Ask user for amount they will spend on food
food_expense = float(input("Enter the amount you will spend on food: "))

# Step 8: Add expenses
total_expenses = gas_expense + accommodation_expense + food_expense

# Step 9: Subtract expenses from budget
remaining_budget = budget - total_expenses

# Step 10: Display results
print(f"\nTravel Destination: {destination}")
print(f"Total Budget: ${budget:.2f}")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Budget: ${remaining_budget:.2f}")
