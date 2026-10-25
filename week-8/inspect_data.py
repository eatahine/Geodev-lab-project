import csv
def inspect_column(filename, column):
    with open("sap_pop2.csv", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)


    values = []
    for row in rows:
        value = float(row[column].strip())
        if value == "":
            continue
        values.append(value)
    return {
        "smallest":min(values),
        "largest":max(values),
        "average":sum(values)/len(values),
        "count":len(values)
    }
area_result = inspect_column("sap_pop2.csv", "area")
population_result = inspect_column("sap_pop2.csv", "population")
print(area_result, "area_result")
print(population_result, "population result")