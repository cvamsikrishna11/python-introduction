# The if statement alone tells us that if a condition is true it will execute a block of statements and if the condition is false it won’t. 
# But what if we want to do something else if the condition is false. 
# Here comes the else statement. 
# We can use the else statement with if statement to execute a block of code when the condition is false. 

# python program to illustrate if-else statement
# if-else condition - example 1
print('\n # if-else condition - example 1')
age = 20
if (age < 18):
	print("No kid your not allowed")	
else:
	print("welcome big guy")
print("Play the music!")


# # # if-else condition - example 2
print('\n # if-else condition - example 2')
is_train_in_two_miles = True
if is_train_in_two_miles == True:
    print("close the gate")
else:
    print("don't close the gate")
print('Line outside the if-else block')