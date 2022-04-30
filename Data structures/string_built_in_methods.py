# string will come under the default data types itself but in this file the aim is to understand string operations & built-in methods
# string can be defined in either in double quotes or single quotes

name = "vamsi"
price = "$100"
quantity = " 10 items "

# printing string values
print("\n# printing string values")
print(name)
print(price)
print(quantity)


# print type
print("\n# print type")
print(type(name))


# # check if specific character present in string
print("\n# check if specific character present in string")
print('a' in name)

# # length of string
print("\n# length of string")
print(len(name))
print(len(quantity))

# # access specific element in the string with index
print("\n# access specific element in the string with index")
print(name[0])  # forward indexing
print(name[2])
print(name[3])
print(name[-1])  # reverse indexing
# print(name[5]) # string index outt of range


# # string slicing --> to get the specific subset of string
print("\n# string slicing --> to get the specific subset of string")
print(quantity)
print(quantity[2:5])
print(price[:2])


# # # check string methods and attributes with dir() method
print("\n# check string methods and attributes with dir() method")
print(dir(name))

# # # replace string elements
print("\n# replace string elements")
new_name = name.replace('v', 'V')
print(new_name)
new_quantity = quantity.replace('10', '100')
print(new_quantity)

# # remove white spaces from the beginning or end of a string
print("\n# remove white spaces from the beginning or end of a string")
new_quantity = quantity.strip()
print("quantity:",quantity,",length:",len(quantity))
print("quantity:",new_quantity,",length:",len(new_quantity)) # use debugger and show the diff

# # # convert string characters to upper or lower case
print("\n# convert string characters to upper or lower case")
new_quantity = quantity.upper()
print(quantity, new_quantity)
new_quantity = quantity.lower()
print(quantity, new_quantity)


# # # split string based on values
print("\n# split string based on values")
msg = "Hello, world!"
new_msg = msg.split(",")
print(new_msg)
email = "vamsi.krishna.chunduru@jjtech.com"
new_email = email.split("@")
print(new_email)
print(new_email[1])
company_name = new_email[1].split(".")
print(company_name)
print(company_name[0])