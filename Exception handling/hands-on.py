from unittest import result


#print("Yes!!")

# marks = 84
# try:
#     result = marks/0
#     print(result)
# except ZeroDivisionError:
#     print("Please don't divide with 0")
# except:
#     print("Unknown error..")

# print("Hellooooo....")


# age = input("Please enter your age >")

# try:
#     print(age + "old")
# except Exception as e:
#     print(e)
#     print("You should only use string and not int")


try:
    f = open("sports.txt", "r")
    print("Open in read mode!")
except Exception as e:
    print("File not found creating new file!")
    f = open("sports.txt", "x")
finally:
    print("Closing file")
    f.close()