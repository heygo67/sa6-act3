# Define the two lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Use filter() with a lambda function to find the intersection of the two lists
intersection = list(filter(lambda x: x in list1, list2))

# Print the intersection
print("Intersection of the two lists:", intersection)
