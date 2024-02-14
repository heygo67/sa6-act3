# Define the list of numbers
numbers = [1, 2, 3, 4, 5]

# Define the constant value
n = 3

# Use map() with a lambda function to raise each number to the power of n
result = list(map(lambda x: x ** n, numbers))

# Print the result
print("Numbers raised to the power of", n, ":", result)
