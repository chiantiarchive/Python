from dataclasses import dataclass
from datetime import date


@dataclass
class Invoices:
    invoice_no: str
    client: str
    amount: float
    due: date
    paid: bool = False


    def days_overdue(self, today: date) -> int:
        return (today - self.due).days


    def is_overdue(self, today: date) -> bool:
        return not self.paid and self.days_overdue(today) > 0