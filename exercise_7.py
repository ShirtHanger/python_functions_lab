# Exercise 7: Calculate a Tip
#
# Create a function called `calculate_tip`. It should take the bill amount and the tip percentage (as a whole number).
# The function should return the amount of the tip.
#
# Examples:
# calculate_tip(50, 20) should return 10.
#
# Write your function and test its output below.

def calculate_tip(bill, tip):
    percent = (tip / 100)
    final_tip = bill * percent
    return f'You should tip them {final_tip}%'



print('Exercise 7:', calculate_tip(50, 20))
