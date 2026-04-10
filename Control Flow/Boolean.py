print(True) # yes in english
print(False)  # no in english

print(type(True))  # <class 'bool'>
print(type(False)) # <class 'bool'>

print(bool(123))  # True
print(bool("Hi")) 
print(bool(""))    # False

print(bool(0))   # False
print(bool(0.0)) # False
print(bool([]))  # False
print(bool(()))  # False
print(bool({}))  # False
print(bool(None)) # False
print(bool(1))   # True
print(bool(-1))  # True
print(bool([1, 2, 3])) # True
