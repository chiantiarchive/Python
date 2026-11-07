orders = [
    {"customer": "chianti", "amount": 120.0},
    {"customer": "chivara", "amount": 80.5},
    {"customer": "serene", "amount": 45.0},
    {"customer": "chi", "amount": 300.0},
]

totals = {}
for order in orders:
    name = order["customer"]
    totals[name] = totals.get(name, 0) + order["amount"]

ranked = sorted(totals.items(), key=lambda pair: pair[1], reverse=True)
for rank, (name, total) in enumerate(ranked, start=1):
    print(rank, name, f"{total:,.2f}")