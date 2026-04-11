# check if a usersname is not empty and the age is greater than or equal
# to 18

# username = "Tom"
# age = 21

# print(username is not None and age >= 18)


# Check if the password is more than 8 characters.
# password = input("Enter our Password:\n")

# if len(password) >= 8:
#     print("Password is Valid")
# else:
#     print("password needs to be more than 8 Characters")

# Check is users mailbox is not empty and contains a '@' and ends '.com'

# email = input("Please enter your email address\n")

# if email.endswith(".com") and email != "" and "@" in email:
#     print("This is a valid email")
# else:
#     print("This is not a valid email")

# username = input("Please enter your username\n")
# count = len(username)

# if isinstance(username, str) is not None and len(username)>= 5:
#     print("Valid username")
# else:
#     print("Invalid username, please enter again")
#     print(f"Your username is only {count}  in length")

#Check if the user is either an admin or a moderator
#and either they're not banned or they've verified their email

# Sample user data
role = input("Please enter role, admin, moderator or user\n")         # could be "admin", "moderator", "user"
is_banned = True       # True or False
email_verified = False   # True or False

# Check condition
if (role in ["admin", "moderator"]) and (not is_banned and email_verified):
    print("Access granted")
else:
    print("Access denied")