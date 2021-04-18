# WHILE LOOPS EXERCISES

# Enter a random string in the variable string_1,
# then enter a character and save it in the variable char_1.
# Write code, which will count how many times your character is included in your string.
# Save result to result_1 variable

string_1 = 'Pretty big interesting book'
char_1 = 'i'
result_1 = 0
for char in string_1:
    if char == char_1:
        result_1 += 1
#print(result_1)

result_1_2 = 0
cursor = 0
while cursor < (len(string_1) - 1):
    cursor += 1
    if string_1[cursor] == char_1:
        result_1_2 += 1
#print(result_1_2)

# Enter a random number and save it in variable number_1.
# Then create code to multiply all the digits together
# and save result in the result_2 variable.

number_1 = '234152'
result_2 = 1
for i in number_1:
    result_2 *= int(i)
#print(result_2)

# Enter a random number and save it in variable number_2.
# Then create code which will return a number with digits of number_1 in reverse order.
# Save it in result_3 variable

number_2 = '6305035'
result_3 = ''
counter = len(number_2)-1
print(counter)
while counter >= 0:
    result_3 += number_2[counter]
    counter -= 1
print(int(result_3))