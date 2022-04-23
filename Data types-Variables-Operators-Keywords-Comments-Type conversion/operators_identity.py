# is and is not are the identity operators both are used to check if two values are located on the same part of the memory. Two variables that are equal do not imply that they are identical. 

a = 10
b = 20
# c = a
c = 10

print(a is not b)
print(a is c)

m = "abcd"
print("abc" is m)
print("abcd" == m)