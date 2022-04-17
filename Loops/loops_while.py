# Python While Loop is used to execute a block of statements repeatedly until a given condition is satisfied.

# For loops are used when you want to do operations on each member of a sequence, in order. While loops are used when you need to: operate on the elements out-of-order, access / operate on multiple elements simultaneously, or loop until some condition changes from True to False.
"""
Syntax:
while expression:
    statement(s)
"""

# Python program to illustrate
# while loop example -1
print('\n# while loop example -1')
count = 0
while (count < 5):
    count = count + 1
    print("Hello JJTech, increasing")

# while loop example -2
print('\n# while loop example -2')
count = 10
while (count > 1):
    count = count - 1
    print("Hello JJTech, decreasing")

# example of infinite while loop
print('\n# example of infinite while loop')
count = 0
# while (count < 5):
# 	print("Hello JJTech, infinite loop")
