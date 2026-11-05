import csv
from pathlib import Path

csv_clients = Path(__file__).parent / "clients.csv"

rows = []
with csv_clients.open("r", newline="", encoding="utf-8-sig") as f:
    for row in csv.DictReader(f):
        try:
            row["budget"] = float(row["budget"])
            rows.append(row)
        except ValueError:
            print("Skipping bad row:", row)

print(rows)