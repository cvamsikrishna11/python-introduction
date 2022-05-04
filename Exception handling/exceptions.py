# # to explain the logical error or exceptions concept
# """
# When in the runtime an error that occurs after passing the syntax test is called exception or logical type.
# We have majorly two types of exceptions 1. Logical 2. Runtime
# https://en.wikibooks.org/wiki/Python_Programming/Errors
# """

# # Exception example - 1
# print("\n# Exception example - 1 (Logical)")
# # marks = 85
# # result = marks / 0
# # print("results: {}".format(result))


# # Exception handling for the example-1(Logical example)
# print("\n# Exception handling for the example-1(Logical example)")
# try:
#     marks = 85
#     result = marks / 0
#     print("results: {}".format(result))
# except ZeroDivisionError:
#     print("Seems like you are divding a number with zero which should not work, please check your input!")

# except:
#     print("Something unexpected has happend, please contact the support team!")


# #Counting Sheep
# Goal: Print number of sheep up until 101.
# print("\n# Exception example - 2 (Logical)")# 
# sheep_count=1
# while sheep_count<100:
#     print("%i Sheep"%sheep_count)

# # Exception example - 3 (Runtime)
# # file_data = open("movies_data.csv", "r")
# # print(file_data.read())

# # Exception handling for the example-3(Runtime example)
# print("\n# Exception handling for the example-2(Runtime example)")
# try:
#     file_data = open("movies_data.csv", "r")
#     print(file_data.read())
# except FileNotFoundError:
#     print("Seems like the requested file isn't available, please check if the file name is correct!")
# except:
#     print("Something wrong happend, please check your input or contact admin!")

# # Exception example - 4 (Logical) & raising an error
# print("\n# Exception example - 4 (Logical)")
# def send_amount(tot_amount, amount_to_transfer):
#     if tot_amount >= amount_to_transfer:
#         print('Amount transer successful. Amount sent: {}, Remaining balance: {}'.format(
#             amount_to_transfer, tot_amount-amount_to_transfer))
#     else:
#         raise ValueError("Not sufficient amount")

# try:
#     account_balance = 100
#     transfer_amount = 150
#     send_amount(account_balance, transfer_amount)
# except Exception as e:
#     print("Exception: {}".format(e))

# # Exception handling - another example when wrong data type of the input
# print("\n# Exception handling - another example")
# inp = input('Enter Fahrenheit Temperature:')
# try:
#     fahr = float(inp)
#     cel = (fahr - 32.0) * 5.0 / 9.0
#     print(cel)
# except:
#     print('Please enter a number')

# # The try statement in Python has an optional finally block.
# # It means that it executes the block by all means.
# # At the same time, it releases external resources. 
# print("\n# learning finally block usage")
# try:
#    file = open("Exception handling\my_file.txt", "w")
#    file.write("Hi there, we are learning exception handling!")
#    # this performs file operations
# except:
#     print("File not found")
# finally:
#    file.close()
#    print("Closing file & DB connections!")

