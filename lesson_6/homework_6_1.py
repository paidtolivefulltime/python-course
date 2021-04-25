# You are given a list in list_1 variable, write a swap_first_last function to return a new list with
# the first and the last elements of the list swapped.
# Return this list
# import math

list_1 = [1, 'asdasd', True, 2, False, 4, 'Hello world', None, range(1, 11), 100]


def swap_first_last(array_1):
    array_1[0], array_1[-1] = array_1[-1], array_1[0]
    print(array_1)


swap_first_last(list_1)
print('\n')

# You are given a list in list_2 variable, write a reverse_list function which creates a new list in reversed order.
# Return this list

list_2 = [1, 'asdasd', True, 2, False, 4, 'Hello world', None, range(1, 11), 100]


def reverse_list(array_2):
    array_2.reverse()
    return array_2


print(reverse_list(list_2))
print('\n')

# Create a list which contains only number items and save it to the list_3 variable. Then write multiply_list_items
# function to multiply all the items in a list. Return result of multiplication

list_3 = [1, 5, 7, 11]


def multiply_list_items(array_3):
    result = 1
    for i in array_3:
        result *= i
    return result


print(multiply_list_items(list_3))
print('\n')

# Create a list which contains only number items and save it to the list_4 variable. Then write a smallest_item_list
# function to get the smallest number from a list. Return smallest element

list_4 = [10, 2, 5, 5, 0]


def smallest_item_list(array_4):
    smallest = array_4[0]  # (-math.inf)
    for i in array_4:
        if i < smallest:
            print(f'{i} is smaller than {smallest}, reassigning')
            smallest = i
        else:
            print(f'{i} is not smaller than {smallest}')
    return smallest


print(smallest_item_list(list_4))
print('\n')

# Given a list in list_5 variable, write a remove_duplicates_list function to remove duplicates from a list.
# Return new list without duplicates

list_5 = [1, 2, 3, 1, 1, 1, 2, 3, 4, 'hello', 1, 2, 3, 4, 'hello', 'hello', 1]


def remove_duplicates_list(array_5):
    result = []
    # result.append(x) for i in array_5 if i not in result
    for i in array_5:
        if i not in result:
            result.append(i)
    return result


print(remove_duplicates_list(list_5))
print('\n')

# You are given a list in list_6 variable.Enter an integer number and save it to number_1 variable,
# write a longer_words_list function which will return the list of words that are longer than number_1
# from a given list of words.
number_1 = 5
list_6 = ['On', 'it', 'differed', 'repeated', 'wandered', 'required', 'in.', 'Then', 'girl', 'neat', 'why', 'yet',
          'knew', 'rose', 'spot.', 'Moreover', 'property', 'we', 'he', 'kindness', 'greatest', 'be', 'oh', 'striking',
          'laughter.', 'In', 'me', 'he', 'at', 'collecting', 'affronting', 'principles', 'apartments.', 'Has',
          'visitor', 'law', 'attacks', 'pretend', 'you', 'calling', 'own', 'excited', 'painted.', 'Contented',
          'attending', 'smallness', 'it', 'oh', 'ye', 'unwilling.', 'Turned', 'favour', 'man', 'two', 'but', 'lovers.',
          'Suffer', 'should', 'if', 'waited', 'common', 'person', 'little', 'oh.', 'Improved', 'civility', 'graceful',
          'few', 'smallest', 'screened', 'settling.', 'Likely', 'active', 'her', 'warmly', 'has.']


def longer_words_list(array_6, number1):
    new_longer_words_list = []
    for word in array_6:
        if len(word) > number1:
            new_longer_words_list.append(word)
    return new_longer_words_list


print(longer_words_list(list_6, number_1))
print('\n')

# Given two lists in list_7 and list_8 variables. Write a function find_item_lists that takes two lists and returns
# True if they have at least one common member.
list_7 = [1, 2, 3, 1, 1, 1, 2, 3, 4, 'hello', 1, 2, 3, 4, 'hello', 'hello', 1]
list_8 = ['asdasd', True, 8, False, 94, 'Hello world', None, range(1, 11), 100, 1]


def find_item_lists(array_7, array_8):
    for item in array_7:
        if item in array_8:
            return True
    return False


print(find_item_lists(list_7, list_8))
print('\n')

# You are given a list in list_9 variable. Write a function list_to_string to convert a list of
# characters into a string.
list_9 = ['I', ' ', 'l', 'i', 'k', 'e', ' ', 'P', 'y', 't', 'h', 'o', 'n']


def list_to_string(list9):
    result = ''
    for char in list9:
        result += char
    return result


print(list_to_string(list_9))
print('\n')


# Given a list of numbers in list_10 and a number number_2, write count_items_list function which will count number of
# occurrences of number_2 in the given list
list_10 = [1, 2, 3, 1, 1, 1, 2, 3, 4]
number_2 = 3


def count_items_list(array_10, number2):
    count = 0
    for number in array_10:
        if number == number2:
            count += 1
    return count


print(count_items_list(list_10, number_2))
print('\n')


# Given a list of numbers, write a function even_items_list to return new list which include all even numbers in
# given list.
list_11 = [1, 2, 3, 1, 1, 1, 2, 3, 4]


def even_items_list(array_11):
    result = []
    for number in array_11:
        if number % 2 == 0:
            result.append(number)
    return result


print(even_items_list(list_11))
