
# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

while size <= 0:
    print("Please enter a positive integer.")
    size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Generate the square pattern
while row < size:
    for _ in range(size):
        print("*", end="")  # Print asterisks side by side
    print()  # Move to the next line after each row
    row += 1
