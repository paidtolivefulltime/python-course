 # WHILE LOOPS EXERCISES

# Enter a random string in the variable string_1, then enter a character and save it in the variable char_1.
# Write code, which will count how many times your character is included in your string.
# Save result to result_1 variable

string_1 = 'Pretty Big interesting book'
char_1 = 'i'
result_1 = 0
for char in string_1:
    if char == char_1:
        result_1 += 1
#print(result_1)

result_1_2 = 0
cursor = 0
while cursor < len(string_1)-1:
    cursor += 1
    if string_1[cursor] == char_1:
        result_1_2 += 1
#print(result_1_2)






# Enter a random number and save it in variable number_1. Then create code to multiply all the digits together
# and save result in the result_2 variable.

number_1 = 234152
#number_1 = 789240
result_2 = 1

for i in str(number_1):
    result_2 *= int(i)
#print(result_2)

result_2_1 = 1
digit = 0
string_2 = str(number_1)
while digit < len(str(number_1)):
    #digit+=1
   # print(digit)
   # print(string_2[digit])
    result_2_1 *= int(string_2[digit])

    digit += 1
#print(result_2_1)





# Enter a random number and save it in variable number_2. Then create code which will return
# a number with digits of number_1 in reverse order. Save it in result_3 variable

number_2 = 784015
string_number_2 = str(number_2)
result_3 = str()


string1_index = 0
string2_index = 0
counter = 0
while counter < (len(string_number_2)):
    string1_index = len(string_number_2)-counter-1
    result_3 = result_3 + string_number_2[string1_index]
    counter += 1
print(result_3)