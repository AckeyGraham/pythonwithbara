# checking numeric types

a = 5
b = 3.14
c = 2 + 3j

print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'complex'>

# printing a number in quotes is a string
d = "5"
print(type(d))  # <class 'str'>
# converting string to a number
e = int(d)  # This is telling the program to convert the string "5" into an integer. The int() function takes a string as an argument and returns its integer representation. In this case, it will convert the string "5" into the integer 5.
print(type(e))  # <class 'int'>

# if do a times multiplcation with a string, it will repeat the string that many times
f = "Hello " * 3
print(f)  # Hello Hello Hello

# changing the int to a float
g = 3
print(float(g))  # 3.0 again changing the integer 3 to a float 3.0

h = "3"
print(float(h))  # 3.0 again chaing the string to a float

i = 3
j = 4
print(complex(i, j))  # (3+4j) changing the integers 3 and 4 to a complex number with real part 3 and imaginary part 4