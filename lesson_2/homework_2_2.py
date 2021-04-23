# Change result_string_1 that 'very simple language' will be displayed on a new line

result_string_1 = 'Python is the \n\n\nvery simple language'
print(result_string_1)

# Change result_string_2 to print out the phrase: 'What does the word 'integer' mean'

result_string_2 = 'What does the word \'integer\' mean'
print(result_string_2)

# Assign number variable to value "5" (as a string). Then rise the number to the power 3.
# Save the expression to result_value variable

number = '5'
result_value = int(number) ** 3
print(result_value)


# Enter a random number, then save the value to n variable.
# Finally, you should repeat the variable "word" n times and save the value to result_string_3
import random

n = random.randint(0, 10)
word = 'super'
result_string_3 = word * n
print(result_string_3)

var_str = 'three'
bigger_str = var_str * 5

print(bigger_str.count(var_str))

format_string = 'This is my {} python class{}'
print(format_string.format('2', '!'))

val = 'secret'
print(f'This is my f-string that holds the {var_str} {val}')