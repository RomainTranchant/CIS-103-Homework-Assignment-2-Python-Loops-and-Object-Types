# Romain Tranchant
# CIS 103 Homework Assignment 2:
# Python Loops and Object Types Due 09/13/2024 @11:59pm
# Write a Python program that uses a `for` loop to iterate
# over the string "CIS103" and print character along
# with its ASCII value


# Assigning "CIS103Lab" as a string to the variable string
string = "CIS103Lab3"

# Start a for loop that will iterate every character from the variable string,
# the variable char will take each character of the variable string
for char in string:

# Getting the ascii value with the ord function, with char as an argument
# The ascii value is stored in the ascii_value variable
    ascii_value = ord(char)

# The print function will return every character of "CIS103Lab" and its
# ascii value . The variable {char} will be replaced by its character
# and the variable {ascii_value}
    print(f"Character:{char} Ascii value:{ascii_value}")
