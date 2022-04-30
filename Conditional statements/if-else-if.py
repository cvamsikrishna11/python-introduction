# if --> to handle single case
# if-else --> to handle two cases
# if-else-if --> to handle more than two cases

"""
syntax:

if (condition):
    statement
elif (condition):
    statement
elif (condition):
    statement
.
.
else:
    statement
"""
# if-else-if example
print('\n #if-else-if example')
marks = int(float(input("What is your exam score? ")))
print(marks, type(marks))
if marks >= 85 and marks <= 100:
    print('You got an A! Congrats!')
elif marks >= 75 and marks < 85:
    print('You got a B! Well done!')
elif marks >= 50 and marks < 75:
    print('You got a C. Not great, not terrible.')
elif marks >= 40 and marks < 50:
    print('You got a D. But you can do better!')
else:
    print("You did not pass the exam. Contact the teacher for more information.")
