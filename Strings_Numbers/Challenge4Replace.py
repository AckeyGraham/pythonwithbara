#Convert this messy phone number into a clean one using the replace() method.
#"+49 (176) 123-4567" to clean version.
#Clean numer should look like 00491761234567

phone_number = "+49 (176) 123-4567"
print("Original phone number is ", phone_number)
print("Clean phone number is ", phone_number.replace("+", "00").replace(" ", "").replace("(", "").replace(")", "").replace("-", ""))
