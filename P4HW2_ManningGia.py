# Gia Manning
# 07-07-2024
# P4HW2
# Program however will calculate gross pay for multiple employees, determined by user


def calculate_pay(hours_worked, pay_rate):
    """Calculate regular and overtime pay based on hours worked and pay rate."""
    if hours_worked > 40:
        regular_pay = 40 * pay_rate
        overtime_pay = (hours_worked - 40) * (pay_rate * 1.5)
    else:
        regular_pay = hours_worked * pay_rate
        overtime_pay = 0
    return regular_pay, overtime_pay

# Initialize totals
total_regular_pay = 0
total_overtime_pay = 0
total_gross_pay = 0
employee_count = 0

while True:
    employee_name = input("Enter employee name (or 'Done' to terminate): ")
    if employee_name.lower() == 'done':
        break

    pay_rate = float(input("Enter pay rate: "))
    hours_worked = float(input("Enter hours worked: "))

    regular_pay, overtime_pay = calculate_pay(hours_worked, pay_rate)
    gross_pay = regular_pay + overtime_pay

    # Update totals
    total_regular_pay += regular_pay
    total_overtime_pay += overtime_pay
    total_gross_pay += gross_pay
    employee_count += 1

    print(f"{employee_name}'s regular pay: ${regular_pay:.2f}")
    print(f"{employee_name}'s overtime pay: ${overtime_pay:.2f}")
    print(f"{employee_name}'s gross pay: ${gross_pay:.2f}")

# Display totals
print("\nSummary of payroll information:")
print(f"Total regular pay: ${total_regular_pay:.2f}")
print(f"Total overtime pay: ${total_overtime_pay:.2f}")
print(f"Total gross pay: ${total_gross_pay:.2f}")
print(f"Total number of employees: {employee_count}")

