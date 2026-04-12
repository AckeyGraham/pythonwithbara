# The Rules of this challenge
# - Validate the quality & correctness of Passwords
# - Must not be empty
# - Must include at least one uppercase
# - Must include at least one lowercase
# - Must not be same as the email address
# - Must not contain any spaces
# - Must only start and end with a letter or digit

# email = ""
# password = "HELLO"
# valid = True

# # Clean the string
# password = password.strip()

# # Must not be empty
# if password == "":
#     print("Password cannot be empty")
#     valid - False
# # Must include 1 uppercase
# if not password.upper():
#     print("Password must have one uppercase")
#     valid = False
# #Must include a lowercase
# if not password.lower():
#     print("Password must have one lowercase")
#     valid = False
# if not (password[0].isalnum() and password[-1].isalnum()):
#     print("Email must start or end with a digit or letter")
#     valid = False
# if email == password:
#     print("Password cannot be the same as email address")
# if valid:
#     print("Password is OK")
    
email = "HELLO"
password = "HELLOHELLO"
valid = True

# Clean the string
password = password.strip()

# Must not be empty
if password == "":
    print("Password cannot be empty")
    valid = False

# Must be at least 8 characters
if len(password) < 8:
    print("Password must be at least 8 characters")
    valid = False

# Must include at least 1 uppercase
if not any(c.isupper() for c in password):
    print("Password must have at least one uppercase letter")
    valid = False

# Must include at least 1 lowercase
if not any(c.islower() for c in password):
    print("Password must have at least one lowercase letter")
    valid = False

# Must not contain spaces
if " " in password:
    print("Password must not contain spaces")
    valid = False

# Must not be same as email
if password == email:
    print("Password cannot be the same as email address")
    valid = False

# Must start and end with a letter or digit
if password and not (password[0].isalnum() and password[-1].isalnum()):
    print("Password must start and end with a letter or digit")
    valid = False

# Final result
if valid:
    print("Password is OK")
