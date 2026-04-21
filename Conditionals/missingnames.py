names = ['Rod', 'Jane', 'Tam', 'Freddy']

for name in names:
    if name is None:
        print("Found a missing name")
        break
else:
    print("All names are valid")

# using an else with a break is when else is actually needed in a loop. If a loop without a break, just print outside the loop