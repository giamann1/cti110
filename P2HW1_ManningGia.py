# Gia Manning
# 06-23-2023
# P2HW1




# Function to format money amounts with dollar sign and two decimal places
def format_money(amount):
    return f"${amount:.2f}"

# Function to display travel expenses
def display_travel_expenses(budget, destination, gas, accommodation, food):
    total_expenses = gas + accommodation + food
    remaining_balance = budget - total_expenses

    # Displaying travel expenses
    print("------------Travel Expenses------------")
    print(f"Location:")
    print(destination)
    print(f"Initial Budget:")
    print(format_money(budget))
    print(f"Fuel:")
    print(format_money(gas))
    print(f"Accommodation:")
    print(format_money(accommodation))
    print(f"Food:")
    print(format_money(food))
    print(f"Remaining Balance:")
    print(format_money(remaining_balance))

# Main program
if __name__ == "__main__":
    # Taking input from the user
    budget = float(input("Enter Budget: "))
    destination = input("Enter your travel destination: ")
    gas = float(input("How much do you think you will spend on gas? "))
    accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
    food = float(input("Last, how much do you need for food? "))

    # Calling the function to display travel expenses
    display_travel_expenses(budget, destination, gas, accommodation, food)
