#Searching strings

#search phone number

phone = "+48 123 4567890"

print(phone.startswith("+49"))

#searching email 

email = "alex.graham@virginmedia.com"

print(email.endswith("virginmedia.com"))

#Check extension of a file

file = "report.docx"

print(file.endswith(".docx"))

# check if a string contains a substring


email = "alex.graham@virginmedia.com"

print("@" in email)

#web url
url = "https://api.google.com"

print("/api" in url)

#using find to search for a substring

phone1 = "+48-123-4567890"
phone2 = "48-456-4567890"
phone3 = "0049 123 4567890"

print(phone1[4:])
print(phone2[3:])


print(phone1[phone1.find("-")+1:phone1.find("-", phone1.find("-")+1)])
print(phone2[phone2.find("-")+1:phone2.find("-", phone2.find("-")+1)])
print(phone3[phone3.find(" ")+1:phone3.find(" ", phone3.find(" ")+1)])