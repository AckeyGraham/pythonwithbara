#Challenge One
# Validate the quality and correctness of email values
# - The Rules
# - Must not be empty
# - Must contain '.' and '@'
# - Must contain exactly one '@' symbol
# - Must end with '.com'. '.org' or '.net'
# - Must not be longer thatn 254 characters
# - Must start and end with a letter of digit

email = "alex.graham@email.com"
valid = True
# Clean the string
email = email.strip()


# Must not be empty
if email == "":
    print("Email cannot be empty")
    valid = False
# must contain '.' and '@'
if not ('.'  in email and '@' in email):
    print("email must contain a . and @")
    valid = False
# - Must contain exactly one '@' symbol
if email.count('@') != 1:
    print("You have more than 1 @ in the email")
    valid = False
# Must end with '.com'. '.org' or '.net'
if not email.endswith(('.org','.net', '.com')):# using a set instead of multiple or statements
    print("Please use either .org, .com, or .net at end of email")
    valid = False
#Must not be longer thatn 254 characters
if len(email) > 254:
    print("Email cannot be longer thatn 254 characters")
    valid = False
# Must start and end with a letter of digit
if not (email[0].isalnum() and email[-1].isalnum()):
    print("Email must start or end with a digit or letter")
    valid = False
if valid:
    print("This email is valid")

# To get all statements above showing, we replaced the elif with independent
# if statements , so will return each error if not matching



