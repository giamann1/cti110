# Gia Manning
# 06-30-2024
# P3LAB
# allows the user to enter a money 


def main():
    # Step 1: Input amount of money
    money = float(input("Enter an amount of money as float: (e.g., 12.34): "))
    
    # Step 2: Convert money to cents
    cents = int(round(money * 100))
    
    # Step 3: Calculate number of dollars, quarters, dimes, nickels, pennies
    dollars = cents // 100
    cents %= 100
    
    quarters = cents // 25
    cents %= 25
    
    dimes = cents // 10
    cents %= 10
    
    nickels = cents // 5
    cents %= 5
    
    pennies = cents
    
    # Step 4: Output the result
    result = ""
    
    if dollars > 0:
        result += f"{dollars} {'dollar' if dollars == 1 else 'dollars'} "
    
    if quarters > 0:
        result += f"{quarters} {'quarter' if quarters == 1 else 'quarters'} "
    
    if dimes > 0:
        result += f"{dimes} {'dime' if dimes == 1 else 'dimes'} "
    
    if nickels > 0:
        result += f"{nickels} {'nickel' if nickels == 1 else 'nickels'} "
    
    if pennies > 0:
        result += f"{pennies} {'penny' if pennies == 1 else 'pennies'} "
    
    # Print the final result
    print("The most efficient number of each coin or bill:")
    print(result.strip())

if __name__ == "__main__":
    main()


