"""
To explain the importance of modules and default python modules
https://docs.python.org/3/py-modindex.html
"""


import uuid # https://docs.python.org/3/library/uuid.html#module-uuid
import math # https://docs.python.org/3/library/math.html#module-math
import calendar # https://docs.python.org/3/library/calendar.html#module-calendar
import json # https://docs.python.org/3/library/json.html#module-json

# use methods from uuid module
print("\n# use methods from uuid module")
print(uuid)
print(uuid.uuid4()) 

# use methods from math module
print("\n# use methods from math module")
print(math)
print(math.ceil(10.46)) # returns the ceiling of the smallest integer greater than or equal
print(math.floor(12.8)) # return the floor of x, the largest integer less than or equal to x

# use methods from calendar module
print("\n# use methods from calendar module")
print(calendar)
yy = 2017
mm = 11
print(calendar.month(yy, mm)) # display calendar of given month of the year


# use methods from json module
print("\n# use methods from json module")
print(json)
print(json.dumps({'name': 'vamsi', 'age':21, 'country': 'India'}))




