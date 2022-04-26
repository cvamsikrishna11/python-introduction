# Dictionaries are used to store data values in key:value pairs.
"""
– When you need a logical association between a key:value pair.
"""

student = {"name": "vamsi", "age": "25 years", "college": "abc-college"}
fruits = {"apple": 5, "banana": 3.50, "watermelon": 2.75}
friends = {"class-1": ["david", "ricci"], "class-2": ["john", "matheus"]}

# print dictionary
print('\n # print dictionary')
print(student)
print(fruits)
print(friends)

# access dictionary items
print('\n # access dictionary items')
print(student["name"])
print(fruits.get("apple"))
print(friends["class-2"])

# check if key exists in a dictionary
print('\n # check if key exists in a dictionary')
if 'watermelon' in fruits:
    print(fruits['watermelon'])
else:
    print('requested key not found')

if 'class' in student:
    print(student['college'])
else:
    print('requested key not found')


# check the data structure type of these values
print('\n # check the data structure type of these values')
print(type(student))
print(type(fruits))

# check the methods and attributes available for the dictionary variable
print('\n # check the methods and attributes available for the dictionary variable')
print(dir(student))


# check dictionary length
print('\n # check dictionary length')
print(len(student))
print(len(friends))

# get the keys of dictionary with keys() method
print('\n # get the keys of dictionary with keys() method')
print(student.keys())

# get the values of dictionary with values() method
print('\n # get the keys of dictionary with values() method')
print(student.values())

# copy all the dictionary data into another variable
print('\n # copy all the dictionary data into another variable')
duplicate_student = student.copy()
print(student)
print(duplicate_student)

# modify an existing key value in dictionary
print('\n # modify an existing key value in dictionary')
student['name'] = 'vamsi krishna chunduru'
print(student)

# delete a key from the dictionary
print('\n # delete a key from the dictionary')
if 'college' in student:
    student.pop('college')
    print(student)
else:
    print('key not found')


# add a new key value to dictionary
print('\n # add a new key value to dictionary')
student['college'] = 'abc-college'
print(student)


# iterate over a dictionary keys
print('\n # iterate over a dictionary keys')
for key in student.keys():
    print(key)

# iterate over a dictionary values
print('\n # iterate over a dictionary values')
for val in student.values():
    print(val)

# iterate over a dictionary key,value pairs
print('\n # iterate over a dictionary key,value pairs')
for key,val in student.items():
    print(key, val)


# clear all key-value from dictionary
print('\n # clear all key-value from dictionary')
student.clear()
print(student)

# delete the complete dictionary
print('\n # delete the complete dictionary')
del student
print(student)