# Gia Manning
# 06-30-2024
# P3HW2
# Asks the user to enter name of employee



# Pseudocode algorithm translated into Python

# Step 1: Input Section
employee_name = input("Enter the name of the employee: ")
hours_worked = float(input("Enter the number of hours worked this week: "))
pay_rate = float(input("Enter the employee's pay rate per hour: "))

# Step 2: Calculate Overtime (if any)
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * pay_rate * 1.5
else:
    overtime_hours = 0
    overtime_pay = 0

# Step 3: Calculate Regular Pay
if hours_worked <= 40:
    regular_hours = hours_worked
else:
    regular_hours = 40

regular_pay = regular_hours * pay_rate

# Step 4: Calculate Gross Pay
gross_pay = regular_pay + overtime_pay

# Step 5: Output Section
print("\nEmployee Name:", employee_name)
print("Pay Rate: ${:.2f} per hour".format(pay_rate))
print("Number of Hours Worked:", hours_worked)
print("Overtime Hours:", overtime_hours)
print("Overtime Pay: ${:.2f}".format(overtime_pay))
print("Pay for Regular Hours: ${:.2f}".format(regular_pay))
print("Gross Pay: ${:.2f}".format(gross_pay))

# Step 6: End of Program
