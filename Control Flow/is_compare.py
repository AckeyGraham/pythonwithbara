# using the is logical operator

x = ["a", "b", "c"]
y = ["a", "b", "c"]

print(x == y)  # comparing values
print(x is y)  # comparing ID's

x = 10
y = 10

print(x == y)  # comparing values
print(x is y)  # comparing ID's

x = ["a", "b", "c"]
y = x

print(x == y)  # comparing values
print(x is y)  # comparing ID's

# make sure the email exists

email = ""
print(email != "")  # false as does contain nothing

email = "mail@mail.com"
print(email != "")  # be true as not blank.

email = None
print(email is not "" and email != None)
