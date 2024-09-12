# Romain Tranchant
# CIS 103 Homework Assignment 2:
# Python Loops and Object Types Due 09/13/2024 @11:59pm
# Write a Python program using a `while` loop that prints
# numbers from 1 to 10 but exits the loop early if the number
# is greater than 5


# Giving the value 1 to the variable number
number = 1

# Start a while loop that will run while the variable number
# is smaller or equal to 10 and the print value of number
while number <= 10:
    print(number)

# Increase the value of number by 1
    number += 1

# Check if the value is equal to 6 , the break statement terminates
# the "while" loop, 6 and the rest of the numbers after 6 are not printed
    if number == 6:
        break