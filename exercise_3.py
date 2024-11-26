# Exercise 3: Apply a Discount
#
# Write a function named `apply_discount` that takes a product's price and a discount percentage (from 0 to 100).
# Return the new price after applying the discount.
#
# Examples:
# apply_discount(100, 25) should return 75.
# apply_discount(80, 10) should return 72.
#
# Define your function and call it to display the discounted price.

def apply_discount(price, discount):
    discount_percent = 1 - (discount / 100)
    final_price = price * discount_percent
    return f'${final_price}'



print('Exercise 3:', apply_discount(100, 25))
