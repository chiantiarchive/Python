import csv, random
from datetime import date, timedelta

random.seed(1)
today = date.today()
names = ["Ayesha Rams", "Ben Ten", "Chianti Vdka", "Dan Daman", "Eich Meto", "Fiora Rion"]

rows = []
for i in range(1, 31):
    due = today + timedelta(days=random.randint(-45, 20))
    rows.append({
        "invoice_no": f"INV-{i:03d}",
        "client": random.choice(names),
        "amount": round(random.uniform(100, 5000), 2),
        "due_date": due.isoformat(),
        "paid": random.choice(["yes", "no", "no"]),
    })  

rows[4]["amount"] = "abc"
rows[11]["due_date"] =  "31/02/2026"
rows[19]["client"] = ""

with open("invoices.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)

