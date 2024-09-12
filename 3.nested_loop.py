# Romain Tranchant
# CIS 103 Homework Assignment 2:
# Python Loops and Object Types Due 09/13/2024 @11:59pm
# Write a program to generate the following pattern using nested loops
# *
# **
# ***
# ****

# Starting a for loop with i in rang of the number 1 to 4
for i in range(1,5):

# Starting another loop where j will iterate i from the value 0 to 4
    for j in range(i):

# Print the  "*" character, the "end=" argument prevent the print function
# the stars to be printed after each others, but to be printed on different lines
        print('*', end='')

# All the starts from the previous row were printed , this print function stars
# a new row
    print()
