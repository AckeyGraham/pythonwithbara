import math

# rounding numbers

#measure distance
print(2-10)
#Gives absolute value of the distance
print(abs(2-10))

#rounding numbers
price = 35.5487

print(round(price, 2)) # rounds to 2 decimal places

print(round(price)) # rounds to the nearest whole number

print(math.floor(price)) # rounds down to the nearest whole number

print(math.ceil(price)) 

print(math.trunc(price)) # rounds towards zero, removes the decimal part

#turn the number into an interger
print(int(price)) # truncates the decimal part, similar to math.trunc() 