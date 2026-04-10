#Operators

print(10 == 10) # True
print(10 == 11) # False
print(10 != 10) # False
print(10 != 11) # True
print(10 > 5) # True
print(10 < 5) # False
print(10 >= 10) # True
print(10 <= 9) # False


print("hello" == "hello") # True
print("hello" == "Hello") # False 
print("hello" != "Hello") # True
print("hello" != "hello") # False

# The chain comparison operators
print(1 < 2 < 3) # True
print(1 < 3 < 2) # False

# is age beteween 18 and 30
age = 25
print(18 <= age <= 30) # True
print(18 <= age <= 24) # False