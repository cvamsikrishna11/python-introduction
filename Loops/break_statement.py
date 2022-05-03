# Break statement in Python is used to bring the control out of the loop when some external condition is triggered.
# Break statement is put inside the loop body (generally after if condition).

# Python program to
# demonstrate break statement

s = 'jjtech python @ learning communityfkghikghslghhgisa[j]]qapoweoifrh[o iw hwe]rioweroiwueqriuwqerwe[irwpeoruweqroiwehw'
# Break example using for loop
print("\n# Break example using for loop")
for letter in s:
	print(letter)
	# break the loop as soon it sees '@'
	if letter == '@':
		break

print("\nOut of for loop")
# print()


# Break example using while loop
print("\n# Break example using while loop")
i = 0

# Using while loop
while True:
	print(s[i])
	# break the loop as soon it sees '@'	
	if s[i] == '@' :
		break
	i += 1

print("Out of while loop")
