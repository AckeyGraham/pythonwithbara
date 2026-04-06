#transformations of code
# we are using the .replace() method to change the format of a string, such as changing the decimal separator from a comma to a dot.

price = "1234,56"
print(price)
# We will replace the comman with a dot for currency 
#using the replace() method to change the comma to a dot
price = price.replace(",", ".")
print(price)

# another use case to use the replace() method is to remove unwanted characters from a string, such as spaces or special characters.
phone = "176-1234-56"
print(phone)

phone = phone.replace("-", "/")
print(phone)

# We can also use the replace() method to replace multiple occurrences
# of a substring in a string.
#We will replace the - with a nospace in the phone variable
phone = "176-1234-56"
print(phone)

phone = phone.replace("-", " ")#The no space is like a remove 
print(phone)

# We want rid of decorations
price = "$1,299.99"
print(price.replace("$", "").replace(",", ""))
      