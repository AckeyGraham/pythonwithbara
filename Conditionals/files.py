# are the files CSV

files = ['data1.csv', 'report.pdf', 'report2.csv']

for file in files:
    if not file.endswith(".csv"):
        print(f'{file} is not CSV')
        break
else:
    print(f"{file} contains CSV")
