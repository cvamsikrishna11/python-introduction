# in and not in are the membership operators; used to test whether a value or variable is in a sequence.

# Python program to illustrate
# not 'in' operator
x = 'J'
y = '@'
name = 'JJ Tech'

if (x not in name):
	print("x is NOT present in given list")
else:
	print("x is present in given list")

if (y in name):
	print("y is present in given list")
else:
	print("y is NOT present in given list")
