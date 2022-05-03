# Continue statement is a loop control statement that forces to execute the next iteration of the loop while skipping the rest of the code inside the loop for the current iteration only

# Python program to demonstrate continue statement

# loop from 1 to 10


for i in range(1, 11):	
	# If i is equals to 6,
	# continue to next iteration
	# without printing
	if i == 3:
		continue
	else:
		# otherwise print the value
		# of i
		print(i, end=" ")
	
	
	
