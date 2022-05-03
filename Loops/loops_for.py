# For loops are used for sequential traversal. For example: traversing a list or string or array etc.

# For loops are used when you want to do operations on each member of a sequence, in order. While loops are used when you need to: operate on the elements out-of-order, access / operate on multiple elements simultaneously, or loop until some condition changes from True to False.
"""
Syntax:
for iterator_var in sequence:
    statements
"""

# Iterating over a string
print('\n# Iterating over a string')
word = "JJTech"
for each_letter in word:
    print(each_letter.lower())

# # # Iterating over a list
print('\n# Iterating over a list')
fruits = ["apple", "banana", "watermelon", "grapes"]
for fruit in fruits:
    print(fruit)

# # range() function
# range funtion will return the sequence of numbers one lesser than what we have mentioned
# range(5) will return-->  0,1,2,3,4 in a list
print('\n# range() method example')
print(range(5))

# # # so if we want numbers from 0-9 we dont have to create a specific list for it we can simply write the code as below
print("\n#range from 0-5")
for i in range(5):    
    print("enter your pin?", i)

# # # if we need a starting number from 2
print("\n#range from 2-9")
for i in range(1, 10):
    print(i)

# # # if we need a starting number from 2, if we want to specify the incremental value from 1 to any other number (3 for example)
print("\n#range from 2-9 & with increment of 3")
for i in range(2, 10, 3):
    print(i)

# # # so the range method syntax is --> range(start_value, stop_value, increment_value)
