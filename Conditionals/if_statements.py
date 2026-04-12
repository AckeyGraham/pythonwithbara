# using if statements & else

# score = 80

# if score >= 90:
#     print("True")
# else:
#     print("False")

# elif

# score = int(input("Please give me your score out of 100:\n"))

# if score >= 90:
#     print("What a great score")
# elif score >=70:
#     print("That was an OK score")
# else:
#     print("You did OK")

# branching elif

# score = int(input("Please give me your score out of 100:\n"))

# if score >= 90:
#     print("A Grade")
# elif score >= 80:
#     print("B Grade")
# elif score >= 70:
#     print("C Grade")
# elif score >= 60:
#     print("D Grade")
# else:
#     print("You Failed :-()")

#Nested If

# score = int(input("Please give me your score out of 100:\n"))
# project = True

# if score >= 90:
#     if project:
#         print("A+ Grade")
#     else:
#         print("A Grade")
# elif score >= 80:
#     print("B Grade")
# elif score >= 70:
#     print("C Grade")
# elif score >= 60:
#     print("D Grade")
# else:
#     print("You Failed :-()")

#using and / or in a conditional

# score = int(input("Please give me your score out of 100:\n"))
# project = True

# if score >= 90 and project:
#     print("A+ Grade")
# elif score >= 90:
#     print("A Grade")
# elif score >= 80:
#     print("B Grade")
# elif score >= 70:
#     print("C Grade")
# elif score >= 60 or project:
#     print("D Grade")
# else:
#     print("You Failed :-()")

#Independant IFs

# score = 90
# project = True

# if score >= 90:
#     print("High Score")
# else:
#     print("Low Score")
    
# if project :
#     print("Project Submitted")
# else:
#     print("Project Not Submitted")
    
# Inline If's (Ternary) as above
# score = 55

# print("A" if score >= 90 else "F")

# grade = "A" if score >= 90 else "F"
# print(grade)

# Again converting another elif into a shorter.
score = 50
grade = "A" if score >=90 else "B" if score >= 80 else "F"
print(grade)