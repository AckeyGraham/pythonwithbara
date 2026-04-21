file_list = [
    'reports.csv',
    'data.xlsx',
    'summary.docx',
    'report.csv',
    'data.csv'
]

seen = set()
duplicate_found = False

for v in file_list:
    if v in seen:
        duplicate_found = True
        print(f"Duplicate found: {v}")
        break
    seen.add(v)

if not duplicate_found:
    print("No duplicates found")