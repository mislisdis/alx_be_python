
# Prompt the user to enter a number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print the multiplication table
print(f"\nMultiplication Table for {number}:\n")
for i in range(1, 11):  # Loop through numbers 1 to 10
    product = number * i
    print(f"{number} * {i} = {product}")

