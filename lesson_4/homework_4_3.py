# WHILE LOOPS EXERCISES

# Enter a random string in the variable string_1, then enter a character and save it in the variable char_1.
# Write code, which will count how many times your character is included in your string.
# Save result to result_1 variable

# string_1 = None
# char_1 = None
# result_1 = None
string_1 = 'pretty big int'
char_1 = 'i'
result_1 = 0
for char in string_1:
    if char == char_1:
        result += 1
print(result_1)
-------

string_1 = 'pretty big int'
char_1 = 'i'
result_1 = 0

result_1_2 = 0
cursor = 0 
whle cursor < (len(string_1) - 1):
    cursor +=1
    if string_1[cursor] = char_1:
        result_1_2 += 1
print(result_1_2)
# Enter a random number and save it in variable number_1. Then create code to multiply all the digits together
# and save result in the result_2 variable.
#for
number_1 = 23456
result_2 = 1
for i in str(number_1):
    result_2 *= int(i)
print(result_2)
#while
num = 0
result_2 = 1
num_1 = str(num)
count = len(num_1) 
index = 0 
while (count != 0):
    var_1 = num_1[index]
    var_2 = int(var_1)
    result_2 = result_2 * var_2
    index = index + 1
    count = count - 1 
print(result_2)
  


# Enter a random number and save it in variable number_2. Then create code which will return
# a number with digits of number_1 in reverse order. Save it in result_3 variable
#while
number_2 = '654321'
result_3 = ''
counter = len(str(number_2))-1
while counter >= 0: 
    result_3 += number_2[counter]
    counter -= 1
print(int(result_3))

#for
number_2 = '75747287'
result = ''
for i in number_2:
    result = number_2[::-1]
print(result)
    