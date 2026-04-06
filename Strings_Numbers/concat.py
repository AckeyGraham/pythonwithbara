# learn how to concatunate strings in Python

first_name = "Alex"
surname = "Graham"
full_name = first_name + " " + surname
print(full_name)

#File Path
# To conconatenate you just use the '+' operator.
folder = "C:/Users/Alex/Documents/"
file = "data.txt"
file_path = folder + file
print(file_path)

#F-string

first_name = "Alex"
age = 30
is_student = False

#Using what we have learnt it would look like this:
print("My name is " + first_name + ", I am " + str(age) + " years old and it is " + str(is_student) + " that I am a student.")

#Modern Way - F-string
print(f"My name is {first_name}, I am {age} and it is {is_student} that I am a student.")#Easier to use and readale and same output.

print(f"2+3 = {2+3}") #You can use expressions also in the{} brackets.
#to print the curly brackets you can use double {{}} like this:
print(f"To print curly brackets use double {{}} like this: {{}}")