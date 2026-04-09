#whitespace clean up

text = "  engineering".lstrip()#left side spaces
print(text)

text = "engineering  ".rstrip()#right side spaces
print(text) 
text = "  engineering  ".strip()#Both sides spaces
print(text)

#strips is the best

#What is text is in the middle of the string?

text = "###ABc###".strip("#")#removes the # from both sides by passing in the character to be removed as an argument
print(text)

text = "Engineering"
print(len(text))#Firsly counds all the characters including the spaces and gives the length of the string
print(len(text.strip()))#removes the space and gives the correct length of the string

#gives the number of spaces in the string by subtracting the length
# of the stripped string frminus om the original string
#using the - operator to find the number of spaces in the string
print(len(text) - len(text.strip())) 
#using boolean to check if there are spaces in the string
print(len(text) == len(text.strip()))

nr_of_spaces = len(text) - len(text.strip())
is_clean = len(text) == len(text.strip())
print(f"Number of spaces: {nr_of_spaces}")
print(f"Is the string clean? {is_clean}")