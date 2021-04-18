# WHILE LOOPS EXERCISES

# Enter a random string in the variable string_1, then enter a character and save it in the variable char_1.
# Write code, which will count how many times your character is included in your string.
# Save result to result_1 variable
import random

string_1 = 'The quick red fox jumps over the lazy brown dog'
char_1 = 'T'
result_1 = 0

for i in string_1:
    if i == char_1:
        result_1 += 1
print(result_1)

result_1_1 = 0
counter = 0
while counter < (len(string_1) - 1):
        if string_1[counter] == char_1:
            result_1_1 += 1
        counter += 1
print(result_1_1)



# Enter a random number and save it in variable number_1. Then create code to multiply all the digits together
# and save result in the result_2 variable.

number_1 = '45678'
result_2 = 1

counter_1 = 0
result_2_1 = 1
while counter_1 < (len(number_1)):
    result_2_1 *= int(number_1[counter_1])
    counter_1 += 1
print(number_1, result_2_1)



for i in number_1:
    result_2 *= int(i)
print(number_1, result_2)



# Enter a random number and save it in variable number_2. Then create code which will return
# a number with digits of number_1 in reverse order. Save it in result_3 variable

number_2 = '45678'
result_3 = ''

counter_2 = len(number_2) - 1
while counter_2 >= 0:
    result_3 += number_2[counter_2]
    counter_2 -= 1
print(int(result_3))

number_2_1 = '45678'
result_3_1 = ''
for i in number_2_1[::-1]:
    result_3_1 += i
print(result_3_1)






