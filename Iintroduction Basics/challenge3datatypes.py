#This challenge create's 5 variables, each with a different data type, and then prints the type of each variable to the screen.
# Age / Height / Name / Is Student / No Value yet
# We will then print the values, data types, length of all variables.

age = 49
height = 5.8
name = "Alex Graham"
Student = False
no_value_yet = None

print(age)
print(height)
print(name)
print(Student)
print(no_value_yet)

print(type(age))
print(type(height))
print(type(name))
print(type(Student))
print(type(no_value_yet))

print(len(name))


# Some of the above won't be printed as the len() function doesn't work with all data types, such as NoneType and Boolean.