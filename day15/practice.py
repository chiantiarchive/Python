from dataclasses import dataclass
from datetime import date
from collections import Counter, defaultdict

@dataclass
class Invoice:
    number: str
    client:str
    amount: float
    due_date: date

    def days_overdue(self, today: date) -> int:
        return (today - self.due_date).days


invoices = [
    Invoice("INV-001", "Chianti", 500.0, date(2026, 9, 1)),
    Invoice("INV-002", "Serene", 120.0, date(2026, 10,20)),
    Invoice("INV-003", "Dante", 80.0, date(2026, 9, 15)),
]
today = date(2026, 10, 27)

overdue = [inv for inv in invoices if inv.days_overdue(today) > 0]
by_client = defaultdict(list)
for inv in invoices:
    by_client[inv.client].append(inv)

print(overdue)
print(Counter(inv.client for inv in invoices).most_common())