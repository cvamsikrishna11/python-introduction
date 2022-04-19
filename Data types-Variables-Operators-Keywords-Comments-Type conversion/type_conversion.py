"""
To explain the type conversion concepts
"""

# Example for implicit type conversion
print("\# Example for implicit type conversion")
x = 10

print("x is of type:",type(x))

y = 10.6
print("y is of type:",type(y))

x = x + y

print(x)
print("x is of type:",type(x))



# Example for explicit type conversion
print("\n# Example for explicit type conversion")
# initializing string
s = "10010"

# printing string converting to int
c = int(s)
print ("After converting to integer: {}, type: {}".format(c, type(c)))

# printing string converting to float
e = float(s)
print ("After converting to float : {}, type: {}".format(e,type(e)))


# Example for explicit type conversion while using input
print("\n# Example for explicit type conversion while using input")
age = input("Enter your age? ")
print("Age: {}, Type: {}".format(age, type(age)))
new_age = int(age)
print("Age: {}, Type: {}".format(new_age, type(new_age)))

