# Sample list of strings
strings = ["apple", "banana", "orange", "kiwi", "pear", "grape", "plum"]

# Sort the list based on the length of strings and then alphabetically
sorted_strings = sorted(strings, key=lambda x: (len(x), x))

# Print the sorted list
print(sorted_strings)
