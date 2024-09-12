# Romain Tranchant
# CIS 103 Homework Assignment 2:
# Python Loops and Object Types Due 09/13/2024 @11:59pm
# **Dictionary Operations**:
# Create a dictionary with the following key-value pairs:
# {'name': 'John', 'age': 25, 'city':'New York'}`.
# Write Python code to:
# Add a new key-value pair to the dictionary.
# Update the value of the `age` key.
# Remove the `city` key from the dictionary.
# Print all the keys and values in the diction

# Define the dictionary
the_dictonary = {'name': 'John', 'age': 25, 'city':'New York'}

# Add a new key-value pair to the dictionary
the_dictonary["Country"] = "USA"

# Update the value of the `age` key
the_dictonary["age"] = 26

# Remove the `city` key from the dictionary.
# Print all the keys and values in the diction
del the_dictonary["city"]
print(the_dictonary)

