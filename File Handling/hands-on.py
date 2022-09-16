#file_path = 'C:\\Users\\Damione\\Documents\\sample.txt'
file_path = "C:\\Users\\Damione\\OneDrive\\JJTech\\Python\\python-introduction\\File Handling\\sample.txt"

data = open(file_path, 'r')
# print(data.readline())
# print(data.readline())
#print(data.read())

# for i in data:
#     print(i, end=" ")

#print(dir(data))

data = open(file_path, 'a')
data.write("\nHey will this really work and not overwrite the\nexisting data in the file :/")
#data.close()

print(data.read())
