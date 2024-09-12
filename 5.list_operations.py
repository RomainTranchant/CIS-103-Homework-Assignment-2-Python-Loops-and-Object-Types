# Romain Tranchant
# CIS 103 Homework Assignment 2:
# Python Loops and Object Types Due 09/13/2024 @11:59pm
# **List Operations**:
# Create a list of integers. Write Python code to:
# Append a number to the list.
# Insert a number at a specific index.
# Sort the list in ascending order.
# Pop the last element of the list and print it.
# Remove a specific number from the list.

# Define the_list variable
the_list = [24, 8, 23, 30, 33, 28, 4]

# Add a new number to the list
the_list.append(16)

# Add the number 14 at the index 2, third element
the_list.insert(2, 14)

# Sort the list in ascending order
the_list.sort()

# Remove the last number, index 8, 9th element and print the list
the_list.pop(8)
print(the_list)

# Remove the number 30 and print the list
the_list.remove(30)
print(the_list)