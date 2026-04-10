import random

x = random.randint(1, 100)# Generate a random integer between 1 and 100 (inclusive)
print(x)

print("even" if x % 2 == 0 else "odd") # Check if the number is even or odd using the modulus operator and a conditional expression