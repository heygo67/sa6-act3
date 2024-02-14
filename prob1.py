# Define the lambda function to compute the sum of digits
sum_of_digits = lambda num: sum(int(digit) for digit in str(num) if digit.isdigit())

# Get the input number from the user
number = int(input("Enter a number: "))

# Compute the sum of digits using the lambda function
result = sum_of_digits(number)

# Print the result
print("Sum of digits:", result)
