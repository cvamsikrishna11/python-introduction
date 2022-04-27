# A Tuple is a collection of Python objects separated by commas. In someways a tuple is similar to a list in terms of indexing, nested objects and repetition but a tuple is immutable unlike lists which are mutable.
"""
– Use tuples when your data cannot change.
"""

numbers = (1, 2, 3)
names = ('vamsi', 'avinash', 'showmik')
fruits = ('apple', 'banana', 'orange')
my_tuple = (10, 20, 30, {"name": "vamsi", "age": 22},
            ['car', 'bike', 'bus'], 10)

# print tuples
print('\n # print tuples')
print(numbers)
print(names)
print(fruits)
print(my_tuple)


# verify the type of data structure
print('\n # verify the type of data structure')
print(type(numbers))
print(type(names))


# access tuple items
print('\n# access tuple items')
print(names[0])
print(numbers[1])
print(my_tuple[4])

# check if item exists in the tuple
print('\n # check if item exists in the tuple')
print(10 in numbers)

if 'banana' in fruits:
    print("yes")
else:
    print("no")


# check the methods and attributes available for the tuple variable
print('\n # check the methods and attributes available for the tuple variable')
print(dir(names))

# check tuple length
print('\n # check tuple length')
print(len(names))
print(len(my_tuple))


# get number of times an items is present in the tuple
print('\n # get number of times an items is present in the tuple')
print(my_tuple.count(10))
print(names.count("avinash"))

# get the index of an item in the tuple
print('\n # get the index of an item in the tuple')
print(names.index("vamsi"))
print(fruits.index("orange"))



# iterate over items in the tuple
print('\n # iterate over items in the tuple')
for each_item in names:
    print(each_item)

# modify the tuple WE CANT MODIFY AN EXISTING TUPLE, with the below examples we can understand tuples are immutable
# numbers[0] = 100
# names[1] = 'captain america'
# names.append('iron man')
# names.clear()

# delete the tuple completely
print('\n # delete the tuple completely')
del(names)
print(names)

