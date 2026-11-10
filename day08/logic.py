"""Holds business rules"""


def classify_overdue(days):
    if days <= 0:
        return "On time"
    elif days <= 14:
        return "Friendly reminder"
    elif days <= 30:
        return "Firm reminder"
    else:
        return "Escalate"


def find_overdue(invoices, today):
    overdue = []
    for inv in invoices:
        if inv["paid"]:
            continue
        days_late = (today - inv["due"]).days
        if days_late > 0:
            overdue.append({**inv, "days_late": days_late})
    return overdue