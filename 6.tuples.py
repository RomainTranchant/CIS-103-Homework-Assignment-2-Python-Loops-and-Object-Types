# Romain Tranchant
# CIS 103 Homework Assignment 2:
# Python Loops and Object Types Due 09/13/2024 @11:59pm
# **Tuples**:
# Write a Python program that creates a tuple with 5 elements
# and prints the first and last elements. Then, attempt to
# modify one of the elements and explain the result.

# Define the variable my_tuple
my_tuple = (50,51,52,53,54,55)

# Print the first element , index 0, and the last element , index 5
print("First element", my_tuple[0])
print("Last element", my_tuple[5])

# Try to reassign a different value the to index 2 , element 52 , with
# a new value of 42. This return an error message because tuples can not
# be changed , they are immutables
try:
    my_tuple[2] = 42
except TypeError as t:
    print("Error,", t)