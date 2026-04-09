#Case conversions 

text = "python PROGRAMMING"

print(text.upper()) # Converts to uppercase
print(text.lower()) # Converts to lowercase 

search = "Email".lower() # Converts to lowercase for case-insensitive comparison

data = " emAil".lower() # Converts to lowercase for case-insensitive comparison
print(search == data) # True, because both are converted to lowercase

#The above comes back as false, due to the space in data
#To fix this, we can use the strip() method to remove any leading or trailing whitespace from the data string before comparing it:

search = "Email".lower().strip() # Converts to lowercase for case-insensitive comparison

data = " emAil".lower().strip() # Converts to lowercase for case-insensitive comparison
print(search == data) # True, because both are converted to lowercase