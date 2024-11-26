# Exercise 4: Convert Temperature
#
# Write a function called `convert_temperature` that takes a
# temperature and a unit ('C' for Celsius, 'F' for Fahrenheit)
# and converts the temperature to the other unit.
# The formula for converting Celsius to Fahrenheit is (Celsius * 9/5) + 32.
# The formula for converting Fahrenheit to Celsius is (Fahrenheit - 32) * 5/9.
#
# Examples:
# convert_temperature(0, 'C') should return 32.0.
# convert_temperature(32, 'F') should return 0.0.
#
# Define the function and then call it below.

def convert_temperature(temp, unit):
    imperial_units = ['F', 'fahrenheit']
    metric_units = ['C', 'celsius']
    
    if unit in metric_units: #convert C to F
        converted_temp = (temp * 9/5) + 32
        return f'{temp}°C is equal to {converted_temp}°F'
    elif unit in imperial_units: #convert F to C
        converted_temp = (temp - 32) * (5/9)
        return f'{temp}°F is equal to {converted_temp}°C'
    else:
        return 'Invalid unit system'



print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))
