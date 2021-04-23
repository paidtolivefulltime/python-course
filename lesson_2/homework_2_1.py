# Create three strings using three different methods. Save your result to result_string_1, result_string_2,
# result_string_3 variables

result_string_1 = 'string1'
result_string_2 = "string2"
result_string_3 = '''multi 
                    line
                    string'''
# print(result_string_1, result_string_2, result_string_3)

unicode_example = '\u0041'
# print(unicode_example)


string_var = 'Careerist'
string_var1 = 'is kewl!'
numeric_var = 100
percent_sign = '%'
full_string = string_var + ' ' + string_var1 + ' ' + str(numeric_var) + percent_sign
# print(full_string)

#input_val = input('Enter your name: ')
#print('Hello ' + input_val)

"""
Enter your first and  last name. Join them together with a space in
between. Save a result in a variable result_full_name and
save the length of the whole name in result_full_name_length variable.
"""

"""
var_a = 'a'
test_word = 'January'
if var_a in test_word:
    print('There are letter a in ' + test_word)
else:
    print('There are no letter a in ' + test_word)
"""

first_name = 'Aaron'
last_name = 'Tsang'
result_full_name = first_name + ' ' + last_name
result_full_name_length = len(result_full_name)
# print(result_full_name, result_full_name_length)

# Enter the capital city of California State in lower case. Change the case to title case.
# Save the result in result_ca_capital variable

result_ca_capital = 'sacramento'
print(str.capitalize(result_ca_capital))
# print(str.upper(result_ca_capital))

# Enter the name of our planet. Change the case to upper case. Save the result in
# result_planet variable

result_planet = 'earth'
print(result_planet.title())