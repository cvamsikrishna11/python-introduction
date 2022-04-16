a = 1
b = 'hello'
c = True
d = None

print(a)
print(b)
print(c)
print(d)

# get the type of None, with type keyword
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# example usecase for None

salary = None

if salary is None:
    print('Salary value is not available')
else:
    print('Slary:', salary)
