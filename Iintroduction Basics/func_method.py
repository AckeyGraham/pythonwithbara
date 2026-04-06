# adding variables to the code

text = "Hi"
number = 10
#printing the variables

print(text)
print(number)

# what type are the variables?
type(text) #str
type(number) #int

#these above will not print to screen, therefore we need to print the type of the variables

print(type(text)) #str
print(type(number)) #int

# We will use another nested function with the len fuction
# to print the type of the variables
print(len(text)) #str
#print(len(number)) #int#

# We need to ensure that the built in methods are able to be run again the object type,
#for example .upper can only be used with string objects, therefore it will give an error if we try to use it with an int object.
#bit_length is a method that can be used with int objects, but not with string objects, therefore it will give an error if we try to use it with a string object.
print(text.upper())
print(number.bit_length()) #int does not have the upper method, therefore it will give an error
