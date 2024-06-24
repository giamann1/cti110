# Gia Manning
# 06-23-2023
# P2LAB1
# Find radius



import math

# Read the radius from the user
radius = float(input("Enter the radius: "))

# Calculate the diameter, circumference, and area
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius**2

# Print the results with the specified formatting
print(f"Diameter: {diameter:.1f}")
print(f"Circumference: {circumference:.2f}")
print(f"Area: {area:.3f}")
