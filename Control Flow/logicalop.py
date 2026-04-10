#using the and or not logical operators

print(3 > 1 and 5 < 2)
print(3 > 1 and 5 > 2)


print(3 > 1 or 5 < 2)
print(3 < 1 or 5 < 2)

#checks if the system us under pressure

cpu_usage = 85
memory_usage = 70

print(cpu_usage > 90 or memory_usage > 80)
print(cpu_usage > 80 and memory_usage > 80)
print(cpu_usage < 90 or memory_usage < 80)

#checking user credentials before login
username = True
password = False

print(username and password )# false not both are true

username = True
password = True

print(username and password )# true both are true


username = True
password = False

print(username or password )# true at least one is true

username = False
password = False

print(username or password )# false both are false

#using the not operator to check if a user is not an admin

is_admin = False
print(not is_admin) # true because is_admin is false

is_admin = True
print(not is_admin) # false because is_admin is true

print(not (3 > 1 and 5 < 2)) # true because the original expression is false
print(not (3 > 1 and 5 > 2)) # false because the original expression is true

