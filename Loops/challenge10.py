file_list = [
    "report.csv",
    "data.xlsx",
    "summary.docx",
    "report.csv",
    "data.csv"
]

if len(file_list) != len(set(file_list)):
    print("Duplicate found")
else:
    print("All files are unique")
