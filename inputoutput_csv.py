import csv

# write csv
items = [
    {"name": "Indomie", "price": 3500, "qty": 2},
    {"name": "Aqua",    "price": 3500, "qty": 1},
]

with open("items.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "price", "qty"])
    writer.writeheader()
    writer.writerows(items)

# read csv
with open("items.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)