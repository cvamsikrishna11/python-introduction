# A nested loop is a loop inside the body of the outer loop.
print("\n#nested loops --> exmple - 1")
# outer loop
for i in range(0, 6):    
    # nested loop
    # to iterate from 1 to 5
    for j in range(0, 5):
        # print multiplication
        # default end \n was replaced with a space here to stay at the same line
        print('*', end=' ')
    print()  # use debugger to explain

print("\n#nested loops --> exmple - 2")
# # outer loop
for i in range(1, 11):
    # nested loop
    # to iterate from 1 to 10
    for j in range(1, 11):
        # print multiplication
        # default end \n was replaced with a space here to stay at the same line
        print(i*j, end=' ')
    print()  # use debugger to explain
    
