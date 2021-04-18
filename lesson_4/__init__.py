var = ['apple', 'banana', 'pineapple', 'cherry', 'kiwi']
new_var = var[:3]
# print(new_var)

newer_var = var[1:] # var[1:len(var)]
#print(newer_var)

newest_var = var[:]
#print(var, newest_var)

for i in range(2, -3, -1):
    print(i)