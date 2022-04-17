#  List will be helpful to store multiple items in a single variable.


# list variables
fruits = ["banana", "apple", "watermelon"]
prices = ["$100", "$150", "$10.50"]
numbers = [1, 2, 3, 4, 5]
my_list = [1, "car", 10.40, True]


# printing the list items
print('# printing the list items')
print(fruits)
print(prices)
print(numbers)
print(my_list)

# check the data type
print('# check the data type')
print(type(fruits))
print(type(numbers))


# nested list
print('# nested list')
my_custom_list = [fruits, prices, [6, 10, 2]]
print(my_custom_list)

# peform actions on list
# return attributes and methods of an object
print('# dir() method')
print(dir(fruits))

# append items to existing list
print('# append() method')
fruits.append("kiwi")
print(fruits)

# sort the list
print('# sort() the list')
fruits.sort()
print(fruits)

# length of list
print('# length of the list')
print(len(fruits))

# access a specific element in list
print('# access a specific element in list')
print(fruits[2])
print(fruits[0])

# iterate over all items in the list, one after another
print('# iterate over all items in the list, one after another')
for each_item in fruits:
    print(each_item)

# iterate over each item in the list along with item index
print('# iterate over each item in the list along with item index')
for index, each_item in enumerate(fruits):
    print(index, each_item)

# list with dictionaries inside
print('# list with dictionaries inside')
marks = [{"name": "vamsi", "marks": 50}, {"name": "avinash",
                                          "marks": 60}, {"name": "showmik", "marks": 70}, ]
print(marks)
