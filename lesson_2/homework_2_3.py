# Write your first program. Enter the temperature right now in Fahrenheit in temperature_fahrenheit variable as
# a string (e.g. '75') and convert it to Celsius.
# !important you should save only number to result_temperature. Formula (32°F − 32) × 5/9 = 0°C

# type your code here
temperature_fahrenheit = '75'
result_temperature = (int(temperature_fahrenheit) - 32) * 5/9
print(result_temperature)

format_string = 'This is my {} python class {}'
print(format_string.format('2', '!')) #.format()

val = 'secret'
f_string = 'This is my f-string that holds the {}'
print(f'This is my f-string that holds the {temperature_fahrenheit} { val}')  #f'
print(f_string.format(val))     #.format()
