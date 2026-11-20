import csv
#read file into rows
def read_rows(sap_pop2):
    with open("sap_pop2.csv", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))
#extract and clean values from column
def clean_values(rows, column):
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue
        values.append(float(raw))
    return values
#summarise values
def summarise(values):
    if len(values) == 0:
        return{"count": 0, "smallest": None, "largest": None, "average": None}
    return{
        "count": len(values),
        "smallest": min(values),
        "largest": max(values),
        "average": sum(values)/len(values)
    }
#summarise all
def summarise_all(sap_pop2, columns):
    rows = read_rows("sap_pop2.csv")
    report = {}
    for column in columns:
        values = clean_values(rows, column)
        report[column] = summarise(values)
    return report

report = summarise_all("sap_pop2.csv", ["area", "population"])
for column, stats in report.items():
    print(column, "->", stats)

rows = read_rows("sap_pop2.csv")
values = clean_values(rows, "population")
result = summarise(values)
print(result)