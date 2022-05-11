# The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects. 
# Iterating over a sequence is called traversal.

# Syntax of for Loop

# for val in sequence:
#     loop body

# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
    sum = sum+val

print("The sum is", sum)