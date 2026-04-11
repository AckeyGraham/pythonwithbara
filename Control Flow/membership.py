print("f" not in "python")

# security check: is a domain on the banned list

domain = "spam.com"

blacklist = ["spam.com", "fake.org", "bot.net"]

print(domain not in blacklist)

# so we have learnt to use the membership operators
# "in" & "not"