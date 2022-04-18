"""
Python Functions is a block of related statements designed to perform a computational, logical, or evaluative task.
The idea is to put some commonly or repeatedly done tasks together and make a function so that instead of writing the same code again and again for different inputs, we can do the function calls to reuse code contained in it over and over again.
"""

"""
Syntax:
def function_name(parameters):
    statement
    return expression
"""

# dependencies
import re
import util

# Simple Python function
print("\n#Simple Python function")


def hello():
    print("Hello, welcome to JJtech Python class!")


# Calling the existing function
print("\n# Calling the existing function")
hello()


# Function with arguments
# A simple Python function to check whether x is even or odd
# Here the x --> the data that is being passed to the function is called arguments
print("\n# Function with arguments")
def check_number(x):
    if x > 0:
        print("positive number")
    elif x < 0:
        print("negative number")
    else:
        print("neither positive nor negative number")

# Code to call the function
check_number(-2)
check_number(3)
check_number(0)

# call the functions even from other files
# https://www.w3schools.com/python/ref_string_format.asp
print("\n# call the functions even from other files")
def store_invoice_details(name, price, invoice_id):
    print("Storing invoice details of the customer; {}, price: {}, invoice_id: {}".format(name, price, invoice_id))
    util.get_db_credentials_param(name='abcd')
    print("Got DB credentials secret")
    print("Establising db connection....")
    print("Storing the details into DB...")
    print("Successfully stored invoice details in the DB!")
    return True

store_invoice_details(name="Vamsi", price="$150", invoice_id="invoice-12345")


# return statement
print("\n# return statement")
def sum_of_numbers(a,b):
    c = a + b
    return c
print(sum_of_numbers(10,15))


