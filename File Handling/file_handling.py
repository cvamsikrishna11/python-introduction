# Code base explains the file handling in python
# Python file handling uses the method open()
"""
Syntax:
f = open(filename, mode)

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists
"""

# imports
from os.path import dirname, join
import os

# Access the file in the read mode
print("\n# Access the file in the read mode")
# the path is depends on the OS and depends on the folder, IDE
# file_data = open('sample.txt', 'r')
file_data = open('F:\\trainings\\Python\\python-introduction\\File Handling\\sample.txt', 'r') # an open bug from the vs code side https://stackoverflow.com/questions/51006989/visual-studio-code-filenotfounderror-errno-2-no-such-file-or-directory
print(file_data.read())

# # Lets try to fix the folder path issue, read the file using automated path
print("\n# Lets try to fix the folder path issue, read the file using automated path")
current_dir = dirname(__file__)
file_path = join(current_dir, ".\sample.txt")
file_data= open(file_path, 'r')
print(file_data.read())

# # read first we characters of the file
print("\n# read first we characters of the file")
current_dir = dirname(__file__)
file_path = join(current_dir, "./sample.txt")
file_data= open(file_path, 'r')
print(file_data.read(5))


# # read one line
print("\n# read one line")
current_dir = dirname(__file__)
file_path = join(current_dir, "./sample.txt")
file_data= open(file_path, 'r')
print(file_data.readline(), end="")
print(file_data.readline(), end="")

# # read or print lines iteratively
print("\n# read or print lines iteratively")
current_dir = dirname(__file__)
file_path = join(current_dir, "./sample.txt")
file_data= open(file_path, 'r')
for each_line in file_data:
	# print(each_line, end="")
	print(each_line.split(" "))

# # get all file lines in a list
print("\n\n# get all file lines in a list")
current_dir = dirname(__file__)
file_path = join(current_dir, "./sample.txt")
file_data= open(file_path, 'r')
lines_list = file_data.readlines()
print(lines_list)


# # close the file after usage
# # explain the ROM & RAM and closing files with closing apps in the phone
print("\n# get all file lines in a list")
current_dir = dirname(__file__)
file_path = join(current_dir, "./sample.txt")
file_data= open(file_path, 'r')
print(file_data.read())
file_data.close() # to close file in memory
# print(file_data.read())


# # create a new empty file
# print("\n# create a new empty file")
# current_dir = dirname(__file__)
# file_path = join(current_dir, "./myfile.py")
# file_data = open(file_path, "x")
# file_data.close()


# writing into file
print("\n# writing into file")
current_dir = dirname(__file__)
file_path = join(current_dir, "./new_file.txt")
file_data= open(file_path, 'w') # if exists it will opened in write mode, otherwise a new file will be created and opened in write mode
# file_data.write("Woops! I have overwrote the content!!\n") # but we should understand its overwriting the existing content in "w" mode
file_data.write("Heyyyyy\n") 
file_data.write("hiiiiiiiiiii")
file_data.write("vamsi\n")  # but we should understand its overwriting the existing content in "w" mode
file_data.close()
# read written data now
print("\n# read the above written data")
file_data= open(file_path, 'r')
print(file_data.read())
file_data.close()


# # append the content to the existing file
print("\n# append the content to the existing file")
current_dir = dirname(__file__)
file_path = join(current_dir, "./new_file.txt")
file_data= open(file_path, 'a') # if exists it will opened in write mode, otherwise a new file will be created and opened in write mode
file_data.write("Woops! I have appended the content!!\nHurrayyyyyyyy :)\n") # this would be appended to the existing lines
file_data.close()

# # read the file now
file_data= open(file_path, 'r')
print(file_data.read())
file_data.close()

# copy a file
print("\n# copy a file content to a new file")
# open source file in the read mode
current_dir = dirname(__file__)
src_file_path = join(current_dir, "./sample.txt")
src_file_data= open(src_file_path, 'r')
# open/create destination file the write mode
dest_file_path = join(current_dir, "./duplicate_sample.txt")
dest_file_data = open(dest_file_path, "w")

# # now iterate & read from source file --> write to destination file
for line in src_file_data:
	dest_file_data.write(line)
# close both files once copy action is done
src_file_data.close()
dest_file_data.close()

# # now finally read the newly copied file data
dest_file_data = open(dest_file_path, "r")
print(dest_file_data.read())
dest_file_data.close()


# delete file
print("\n# delete file")
current_dir = dirname(__file__)
file_path = join(current_dir, "./new_file.txt")
os.remove(file_path)
# os.remove(file_path) # what will happen when we try to delete the file that isnt exists

# # so to avoide such file not found issues we can simply put a conditions
print("\n#verifying if the file exists before deletion")
current_dir = dirname(__file__)
file_path = join(current_dir, "./new_file.txt")
if os.path.exists(file_path):
	os.remove(file_path)
else:
	print("file with path: {} not found".format(file_path))

