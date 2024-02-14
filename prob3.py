def find_maximum(numbers, compare):
    if not numbers:
        return None
    
    maximum = numbers[0]
    for num in numbers[1:]:
        if compare(num, maximum) > 0:
            maximum = num
    return maximum

numbers = [3, 8, 1, 6, 2, 9, 4, 5]

# Lambda function to compare two numbers and return the greater of the two
greater = lambda a, b: a if a > b else b

# Finding the maximum number in the list using the lambda function
maximum = find_maximum(numbers, greater)

print("Maximum number:", maximum)
