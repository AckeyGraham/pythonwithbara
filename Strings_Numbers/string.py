name = "Alex"

type(name)

print(type(name))

# The code below won't work as age is a int and rest is string

age = 49
print(type(age))
print("Your Age is " + age)

# The code below will work as we are converting the int to a string using str() function
# The age is converted to a string when using print. It will remain a 
# int when we check the type of age variable. 
# The str() function is only used for the print statement and does not change the data type of the age variable itself.

age = 49
print(type(age))
print("Your Age is " + str(age))


age = age + 5