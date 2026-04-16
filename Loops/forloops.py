
#for loops are used to repeat a block of code a certain number of times
# print("Round: 1")
# print("Round: 2")
# print("Round: 3")
# print("Round: 4")
# print("Round: 5")

# #lets use a for loop to do the same thing
# for i in (1, 2, 3, 4, 5):# using a tuple to loop through the numbers 1 to 5
#     print(f"Round: {i}")

# # we can also use a variable
# items = [1, 2, 3, 4, 5]# using a list to loop through the numbers 1 to 5
# for item in items:
#     print(f"Round: {item}")


# #using string values
# items = "Python" # using a string to loop through the characters in the string
# for item in items:
#     print(f"Round: {item}")

# using the range function to loop through a sequence of numbers
for i in range(2,10,2): # using the range function to loop through the numbers 2 to 8 with a step of 2
    print(f"Round: {i}") 

#interating through data

scores = [90, 80, 70, 60, 50]
total = 0
for score in scores:
    total += score
    print(f"Total score: {total}")
print(f"Final total score: {total}")

#date cleanup with for loops

files = ["data1.csv ", " DATA2.csv", " data3.TXT "]
for file in files:
    file = file.strip().lower().replace('.txt', '.csv')  # using the strip method to remove leading and trailing whitespace and converting to lowercase
    print(f"Processing {file}")