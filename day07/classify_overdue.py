#   Rebuilding from day02\rules.py

def classify_overdue(days: int) -> str:
    if days <= 0:
        return "On time"
    elif days <= 14:
        return "Friendly reminder"
    elif days <= 30:
        return "Firm reminder"
    else:
        return "Escalate"
    
for day in (-3, 0, 1, 14, 15, 30, 31):
    print(day, classify_overdue(day))