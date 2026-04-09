#Turn this messy string into a single clean
#Summary with name, role and age.

#Messy Title  " 968-Maria, ( d@t@ Engineer) ;; 29y  "
#Cleaned version name: Maria | role: data Engineer | age: 29

messy_title = " 968-Maria, ( d@t@ Engineer) ;; 29y  "
#Step 1: Strip the string of whitespace
clean_title = messy_title.strip()
print(clean_title)
clean_title.replace("(", "").replace(")", "")
print(clean_title)
#Step 2: Replace the parentheses with a pipe
clean_title = clean_title.replace("(", "| role:").replace(")", "|")
print(clean_title)
clean_title = clean_title.replace("968-", "name: ").replace(","," ")
print(clean_title)
clean_title = clean_title.replace(";; ", "")
print(clean_title)
clean_title = clean_title.replace("d@t@", "data").replace("29y", "age: 29")
print(clean_title)