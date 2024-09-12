# Romain Tranchant
# CIS 103 Homework Assignment 2:
# Python Loops and Object Types Due 09/13/2024 @11:59pm
# Write a Python function that takes a string and returns it reversed using slicing.
# Write a Python function that formats the following output for given variables:
# Name: John, Age: 30, Salary: $50000.50
# Use appropriate field widths to align the output.

# Define the string that we want to reverse.
original_string = "CIS 103 Homework Assignment 2"

# Define the function to reverse the string by returning a reversed version of
# the original string. The slicing operation [::-1] creates a reversed copy.
# The [::] means that we are taking the entire string and the "-1" index means
# we are moving backwards in the sequence
def reverse_string():
    return original_string[::-1]

# Call the reverse_string function and print the output
print(reverse_string())


# Define the variables name, age and salary
name = "John"
age = 30
salary = 50000.50

# Define the variable formatted by using the f string and
# inputting the defined variables into the string
formatted = f"Name:{name}, Age:{age}, Salary:{salary}"

# Define the format_string function by returning the formatted string
def format_string():
    return formatted

# Print the formatted output
print(format_string())






