#Math

password = "123a1111"

print(len(password))

if len(password) < 8:
    print("Password is too short")  
else:
    print("Password is long enough")


# More Math

text = """"
Python is easy to learn.
Python is a powerful programming language.
Many people love python.
"""
#This method (Count) from the string class "text" variable will
#count how many times the word "Python" appears in the text
#variable and print the result to the screen.
print(text.count("Python"))