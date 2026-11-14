from collections import defaultdict


def classify_overdue(days):
    if days <= 0:
        return "On time"
    elif days <= 14:
        return "Friendly reminder"
    elif days <= 30:
        return "Firm reminder"
    return "Escalate"


def find_overdue(invoices, today):
    return [inv for inv in invoices if inv.is_overdue(today)]


def totals_by_client(invoices):
    totals = defaultdict(float)
    for inv in invoices:
        totals[inv.client] += inv.amount
    return dict(sorted(totals.items(), key=lambda pair: pair[1], reverse=True))