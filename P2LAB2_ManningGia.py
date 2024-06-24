# Gia Manning
# 06-23-2023
# P2LAB2
# will write a program that creates a dictionary where the key and value pairs are as follows.


# Create the dictionary with automobile keys and MPG values
my_dict = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# Get all keys from the dictionary
keys = my_dict.keys()

# Print the keys
print("Available vehicles:")
for key in keys:
    print("- " + key)

# Prompt user to enter a vehicle
vehicle = input("Enter the vehicle from the list above: ")

# Check if the entered vehicle exists in the dictionary
if vehicle in my_dict:
    # Get the MPG for the entered vehicle
    mpg = my_dict[vehicle]

    # Prompt user to enter miles to drive
    miles = float(input("Enter the number of miles you will drive: "))

    # Calculate gallons of gas needed
    gallons_needed = miles / mpg

    # Display gallons of gas needed, rounded to two decimal places
    print(f"You will need {gallons_needed:.2f} gallons of gas for {miles} miles.")
else:
    print("Invalid vehicle entered. Please enter a vehicle exactly as listed.")

