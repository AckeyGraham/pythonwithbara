email = ""
phone = "123-456-7890"
username = "john_doe"

#Allow reginstration if one completed if any field is completed

print(any([email, phone, username])) # True
#Allow reginstration if all fields are completed
print(all([email, phone, username])) # False
#if any variable was blank would return false due


print(isinstance(123, int)) # True
print(isinstance("123", int)) # False

print("hello".endswith("o")) # True
print("hello".endswith("l")) # False
print("hello".startswith("h")) # True