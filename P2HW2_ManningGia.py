# Gia Manning
# 06-23-2023
# P2HW2
# Enter Grades




# Function to calculate average of grades
def calculate_average(grades):
    if len(grades) == 0:
        return 0.0
    return sum(grades) / len(grades)

# Function to format average to two decimal places
def format_average(average):
    return f"{average:.2f}"

# Main program
if __name__ == "__main__":
    # Initialize an empty list to store grades
    grades = []

    # Prompt user to enter grades for each module
    for i in range(1, 7):
        grade = float(input(f"Enter grade for Module {i}: "))
        grades.append(grade)

    # Calculate statistics
    lowest_grade = min(grades)
    highest_grade = max(grades)
    sum_grades = sum(grades)
    average_grade = calculate_average(grades)

    # Displaying results
    print("\n----------------- Results -----------------")
    print(f"Lowest Grade: {lowest_grade}")
    print(f"Highest Grade: {highest_grade}")
    print(f"Sum of Grades: {sum_grades}")
    print(f"Grades Average: {format_average(average_grade)}")
