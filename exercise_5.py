# Exercise 5: Sum to N
#
# Write a function named `sum_to` that takes a single integer n and returns the sum of all integers from 1 to n.
#
# Examples:
# sum_to(6) should return 21.
# sum_to(10) should return 55.
#
# Define the function and then call it below.

def sum_to(num):
    
    total = 0
    for number in range(num + 1):
        total += number
    return total


print('Exercise 5:', sum_to(6))
