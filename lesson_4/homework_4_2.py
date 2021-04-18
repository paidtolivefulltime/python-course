# FOR LOOPS EXERCISES

# Ex. 1
# Enter your name,
# save it in name variable and
# save in result_1 variable your name repeated 3 times (use loops)


name_1 = 'Leena'
result_1 = ''
result_1 = str(result_1)
for i in range (3):
   result_1 += name_1
print(result_1)

# TODO: Here is your code


# Ex. 2
# Modify your previous program so that it will enter your name
# (save it in variable  name_2) and a number
# (save in variable number) and
# then save in result_2 variable your name repeated as many times
# as number_1 is
# (use loops)
'''name_2 = input('Enter your name:  ')
number_1 = int(input('Enter a number:  '))
result_2 = ''

# TODO: Here is your code
for i in range(number_1):
    result_2 += name_2
print(result_2)

'''
# Ex. 3
# Enter a random string, which includes only digits.
# Write code which find a sum of digits in this string
# and save it
# into result_3 variable

string_number_1 = input('enter random digits string:  ') #53257
result_3 = 0

for digit in string_number_1:
    result_3 += int(digit)
print(result_3)

# TODO: Here is your code


# Ex. 4
# Create code which sums up all even numbers
# between 2 and 100 (include 100)
# and save it in result_4 variable

result_4 = 0
for i in range(2,101, 2):
    result_4 += i
print(result_4)

# TODO: Here is your code


result_5 = 0
for i in range(2,101):
    if i % 2 ==0:
        result_5 += i
print(result_5)