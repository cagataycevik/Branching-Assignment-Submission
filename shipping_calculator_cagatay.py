# Express Shipping Rate Calculator
# Author: David Kim
# Last Updated: March 2024

# Print welcome message
print("Welcome to Package Express. Please follow the instructions below.")

# Get weight input from user
weight_input = float(input("Please enter the package weight:\n"))

# Check weight restrictions
if weight_input > 50:
    print("Package too heavy to be shipped via Package Express. Have a good day.")
    exit()

# Get package measurements
width_input = float(input("Please enter the package width:\n"))
height_input = float(input("Please enter the package height:\n"))
length_input = float(input("Please enter the package length:\n"))

# Calculate total dimensions
size_total = width_input + height_input + length_input

# Verify size limits
if size_total > 50:
    print("Package too big to be shipped via Package Express.")
    exit()

# Calculate shipping price
# Price = (width * height * length * weight) / 100
shipping_price = (width_input * height_input * length_input * weight_input) / 100

# Show shipping cost to user
print(f"Your estimated total for shipping this package is: ${shipping_price:.2f}")
print("Thank you!") 