# skip weekends if they are in the loop

days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]

Weekends = ["Saturday", "Sunday"]

for day in days:
    if day in Weekends:
        continue
    print(F'Workday = {day}')
