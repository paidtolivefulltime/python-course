# nested array
nested_array = [[1,2,3],[4,5,6],[7,8,9]]
print(nested_array[1][2])

smaller_array = [17,18,19,20]
array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
print(array)
# array.extend(smaller_array)
# array += smaller_array
# array[::4] = [0,10,100,1000]
del array[::4]
# print('After extension:')
# print('After +=:')
# print('After replacing:')
print('After deleting: ')
print(array)

array_one = [1, 2, 3]
array_two = [1, 2, 3]

if array_one == array_two:
    print(f'{array_one} has similar value to {array_two}')


