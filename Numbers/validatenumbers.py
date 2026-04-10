x = 7.0

print(x.is_integer())

x = 7.1

print(x.is_integer())

# this check what is actually a whole number and not just a number with a .0 at the end.

x = 70

print(isinstance(x, int))# True as checking it's a whole number

x = 70.5
print(isinstance(x, int))# False as checking it's a whole number
print(isinstance(x, float))# True as checking it's a number with a .0 at the end.