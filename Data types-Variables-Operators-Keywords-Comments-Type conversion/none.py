
"""
To explain the None data type
"""
a = 1
b = 'hello'
c = False
d = None

# d= "vamsi"

print(a)
print(b)
print(c)
print(d)
# print(len(d))

# get the type of None, with type keyword
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# example usecase for None

blood_group = None

blood_group="O"
if blood_group is None:
    print('Blood group value is not available')
else:
    print('Blood group:', blood_group)
