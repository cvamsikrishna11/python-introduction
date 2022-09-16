# # # is_class_today = True

# # # if is_class_today == True:
# # #     print("Attend")

# # # print("Take a break!")

# # score = 156
# # score = int(input("What is the student exam score?"))
# # grade = ""

# # if score >= 85 and score <= 100:
# #     print("A")
# #     grade = "A"
# # elif score >= 70 and score < 85:
# #     print("B")
# #     grade = "B"
# # elif score >= 55 and score < 70:
# #     print("C")
# #     grade = "C"
# # elif score >= 45 and score < 55:
# #     print("D")
# #     grade = "D"
# # elif score < 45:
# #     print("FAILED")
# #     grade = "FAILED"
# # else:
# #     print("Invalid Grade!")
# #     grade = "Invalid score"

# # print("Fill grade : {} in the sheet".format(grade))
# # print(f"Fill grade : {grade} in the sheet")

# Num = [1,2,3,4,5]

# for i in Num:
#     print(i+1)

# name = "Johnny"

# for char in name:
#     print(char.upper())

marks = (75, 86, 99, 12, 43)
grade = "A"

for each_mark in marks:
    if each_mark >= 85 and each_mark <= 100:
        print("A")
        grade = "A"
    elif each_mark >= 70 and each_mark < 85:
        print("B")
        grade = "B"
    elif each_mark >= 55 and each_mark < 70:
        print("C")
        grade = "C"
    elif each_mark >= 45 and each_mark < 55:
        print("D")
        grade = "D"
    elif each_mark < 45:
        print("FAILED")
        grade = "FAILED, Contact the administrator"
    else:
        print("Invalid Grade!")
        grade = "Invalid score"

# print("Fill grade : {} in the sheet".format(grade))
print(f"Fill grade : {grade} in the sheet")
