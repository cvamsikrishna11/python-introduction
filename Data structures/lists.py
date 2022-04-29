#  List will be helpful to store multiple items in a single variable.

"""
– Use lists if you have a collection of data that does not need random access. Try to choose lists when you need a simple, iterable collection that is modified frequently.
"""


# list variables
fruits = ["banana", "apple", "watermelon", "kiwi", "grapes"]
prices = ["$100", "$150", "$10.50"]
numbers = [1, 2, 3, 4, 5]
my_list = [1, "car", 10.40, True]


# printing the list items
print('\n# printing the list items')
print(fruits, id(fruits))
print(prices)
print(numbers)
print(my_list)

# # check the data type
print('\n# check the data type')
print(type(fruits))
print(type(numbers))


# # nested list
print('\n# nested list')
my_custom_list = [fruits, prices, [6, 10, 2]]
print(my_custom_list)


# # length of list
print('\n# length of the list')
print(len(fruits))

# # access a specific element in list
print('\n# access a specific element in list')
print(fruits[2])
print(fruits[0])
print(fruits[-1])
print(fruits[-2])

# # slicing lists
print('\n# slicing lists')
print(fruits[0:2])
print(fruits[1:4])
print(fruits[1:])


# # peform actions on list
# # return attributes and methods of an object
print('\n# dir() method')
print(dir(fruits))

# # modify particular index of list with new item
print('\n # modify particular index of list with new item')
print(prices)
prices[1] = '$1000'
print(prices)

# # append items to existing list
print('\n# append() method')
fruits.append("mango")
print(fruits)

# sort the list
print('\n# sort() the list')
fruits.sort()
print(fruits)

# # insert item at a particular index
print('\n# insert item at a particular index')
fruits.insert(1,'grapes')
print(fruits)

# remove an item from the list
print('\n# remove an item from the list')
fruits.remove('watermelon')
print(fruits)

# # iterate over all items in the list, one after another
print('\n# iterate over all items in the list, one after another')
for fruit in fruits:
    print(fruit)

# # iterate over each item in the list along with item index
print('\n# iterate over each item in the list along with item index')
for index, each_item in enumerate(fruits):
    print(index, each_item)

# # list with dictionaries inside
print('\n# list with dictionaries inside')
marks = [{"name": "vamsi", "marks": 50}, {"name": "avinash",
                                          "marks": 60}, {"name": "showmik", "marks": 70}, ]
print(marks)


# # clear a list
print('\n # clear a list')
fruits.clear()
print(fruits)

# # delete the complete list
print('\n # delete the complete list')
del(fruits)
print(fruits)