import csv
import json


with open('Audi.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open('Audi80.json', 'w') as f:
    json.dump(rows, f)