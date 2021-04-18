# WHILE LOOPS EXERCISES
'''
# Enter a random string in the variable string_1,
# then enter a character and save it in the variable char_1.
# Write code, which will count how many times your character
# is included in your string.
# Save result to result_1 variable

string_1 = 'Pretty big interesting book'
char_1 = 'i'
result_1 = 0

for char in string_1:
    if char == char_1:
        result_1 += 1
print(result_1)

result_1_2 = 0
cursor = 0
while cursor < (len(string_1) -1):
    cursor += 1
    if string_1[cursor] == char_1:
        result_1_2 += 1
print(result_1_2)


#------------------------------------------------------------
# Enter a random number and save it in variable number_1.
# Then create code to multiply all the digits together
# and save result in the result_2 variable.

# do with while loop
number_1 = 23415
result_2 = 1
for i in str(number_1):
    result_2 *= int(i)
print(result_2)

#another way
number_1 = '23415'
result_2 = 1
for i in number_1:
    result_2 *= int(i)
print(result_2)
'''

# ----------Python Homework using while loop created by Leena ---------
number_1 = '23415'
cursor = 0
result_3= 1
while cursor < (len(str(number_1))):
    result_3 *= int(number_1[cursor])
    cursor += 1

print("Multiplication of digits using while loop: " + str(result_3))
# ----------Python Homework using while loop created by Leena ---------



#--------------------------------------------------------------------
# Enter a random number and save it in variable number_2.
# Then create code which will return
# a number with digits of number_1 in reverse order.
# Save it in result_3 variable
'''
number_2 = '6305035'
result_3 = ''
counter = len(number_2)-1
print(counter)
while counter >=0:
    result_3 += number_2[counter]
    counter -= 1
print(int(result_3))
'''
#------------------------Python homework using For loop created by Leena-------

number_2 = '1234567890'
result_4 = ''
counter = len(number_2)-1

for i in number_2:
    result_4 += number_2[counter]
    counter -= 1
print("Number reversed is: " + result_4)

#------------------------Python homework using For loop created by Leena-------