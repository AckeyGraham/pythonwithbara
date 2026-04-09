#INdexing and slicing
text = "Python"

#Extract the first character using positive index & negative index

print(text[0])#should get the letter 'P'

print(text[-6])#should also get the letter 'P' using negative index

#extract the last character using positive index & negative index

print(text[5]) #should get the letter 'n'
print(text[-1])#should also get the letter 'n' using negative index

#Lets get slicing
date = "2024-06-01"

#extract the year using slicing
print(date[0:4])#This will get the characters from index 0 to 3 (4 is exclusive)
print(date[:4])#This will also get the characters from index 0 to 3 (4 is exclusive) as the start index is not specified it defaults to 0.

#extract the month using slicing
print(date[5:7])#This will get the characters from index 5 to 6 (7 is exclusive)

#extract the day using slicing
print(date[8:])#This will get the characters from index 8 to the end of the string as the end index is not specified it defaults to the length of the string.