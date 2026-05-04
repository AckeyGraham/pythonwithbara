# Match Cases

country = "United States"
if country == "United States":
    print("USA")
elif country == "india":
    print("IN")
else:
    print("Unknown Country")

# The above is very long way to get all the code, hence match case

match country:
    case "United States":
        print("USA")
    case "India":
        print("IN")
    case "Egypt":
        print("EG")
    case "Germany":
        print("DE")
    case _:
        print("Unknown Country")

# Easy to read above.
