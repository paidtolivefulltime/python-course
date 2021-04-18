var = ['apple', 'banana', 'pinnapple', 'cherry']
new_var = var[:3]
print(new_var)

newer_var = var[1:] # var[1:len(var)]
print(newer_var)

newest_var = var[:] # clone
print(newest_var)

print(range(3))

for i in range(4):
    print(i)

for i in range(4,10, 2):
    print(i)

for i in range(2,-3, 1): # no output
    print(i)

for i in range(2,-3, -1):
    print(i)