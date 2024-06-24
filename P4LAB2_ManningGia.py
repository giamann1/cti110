def display_multiplication_table(num):
    for i in range(1, 13):
        print(f"{num} x {i} = {num * i}")

def main():
    while True:
        user_input = input("Enter an integer (or 'no' to exit): ")
        
        if user_input.lower() == 'no':
            print("Exiting the program.")
            break
        
        try:
            num = int(user_input)
            if num < 0:
                print("Cannot accept negative values. Please enter a non-negative integer.")
            else:
                display_multiplication_table(num)
        except ValueError:
            print("Invalid input. Please enter an integer or 'no' to exit.")
        
        run_again = input("Do you wish to run the program again? (yes/no): ")
        if run_again.lower() != 'yes':
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
