# loop though emails and print the ones that are from a specific sender

emails = [
    'data@gmail.com',
    'baraa@data.com',
    'DROP TABLE USERS;',
    'Maria@gmail.com'
]

for email in emails:
    if ';' in email:
        print("SQL Injection attempt detected!")
        break
    print(f"Checking email: {email}")
