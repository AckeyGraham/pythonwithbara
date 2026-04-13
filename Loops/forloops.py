
#for loops are used to repeat a block of code a certain number of times
# print("Round: 1")
# print("Round: 2")
# print("Round: 3")
# print("Round: 4")
# print("Round: 5")

#lets use a for loop to do the same thing
for i in (1, 2, 3, 4, 5):# using a tuple to loop through the numbers 1 to 5
    print(f"Round: {i}")

# we can also use a variable
items = [1, 2, 3, 4, 5]# using a list to loop through the numbers 1 to 5
for item in items:
    print(f"Round: {item}")


#using string values
items = "Python" # using a string to loop through the characters in the string
for item in items:
    print(f"Round: {item}")
