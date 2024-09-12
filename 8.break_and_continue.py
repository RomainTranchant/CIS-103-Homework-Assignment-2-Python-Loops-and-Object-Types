# Romain Tranchant
# CIS 103 Homework Assignment 2:
# Python Loops and Object Types Due 09/13/2024 @11:59pm
# Break and Continue:
# Write a Python program that uses a `while` loop and breaks out
# of the loop when a certain condition is met. Include an option
# to `continue`, skipping an iteration

#Define the number to find
number_to_find = 4

# Start a while loop, the loop runs until the loop is terminated
while True:

# Print the instructions and ask the user to input a number, defined
# as the user_input variable
    print("Instructions: Find the right number between 1 and 5")
    user_input = input("Type your answer:")

# Check if the user input is different that the number to find
# Return a "Wrong number! try again" message and skip the rest
# Skips to the next iteration of the loop with the continue statement,
# asking the user to guess again
    if user_input != number_to_find:
        print("Wrong number! Try again")
        continue

# Check if the user input is equal to the number to find, and return a message
# The break statement terminates the loop
    if user_input == number_to_find:
        print(f"You entered the right number: {number_to_find}")
        break
