# Exercise 9: Basic Calculator
#
# Create a function named `basicCalculator` that takes three arguments: 
# two numbers and a string representing an operation ('add', 'subtract', 'multiply', 'divide'). 
# Perform the provided operation on the two numbers. In operations where the order of numbers is important, 
# treat the first parameter as the first operand and the second parameter as the second operand.
#
# Examples:
# basicCalculator(10, 5, 'subtract') should return 5.
# basicCalculator(10, 5, 'add') should return 15.
# basicCalculator(10, 5, 'multiply') should return 50.
# basicCalculator(10, 5, 'divide') should return 2.
#
# Define the function and then call it below.

def basicCalculator(num1, num2, operation):
    
    valid_inputs = ['add', 'subtract', 'multiply', 'divide']
    answer = 0
    if operation.lower() not in valid_inputs:
        return 'Invalid operation'
    
    else:
        
        if operation.lower() == 'add':
            answer = num1 + num2
        elif operation.lower() == 'subtract':
            answer = num1 - num2
        elif operation.lower() == 'multiply':
            answer = num1 * num2
        elif operation.lower() == 'divide':
            answer = num1 // num2
        return answer
    
    

print('Exercise 9 Result:', basicCalculator(10, 5, "subtract"))