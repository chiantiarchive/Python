"""Combines both loader and logic"""
from datetime import date

from loader import load_invoices
from logic import classify_overdue, find_overdue

import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Overdue invoice checker")
    parser.add_argument("--input", default="invoices.csv", 
                        help="path to the invoice CSV")
    parser.add_argument("--min-days", type=int, default=1, 
                        help="only show invoices at least this many days late")
    return parser.parse_args()


def main():
    args = parse_args()
    today = date.today()
    invoices, skipped = load_invoices("invoices.csv")
    overdue = find_overdue(invoices, today)
    overdue.sort(key=lambda inv: inv["days_late"], reverse=True)


    filtered =[]
    for inv in overdue:
        if inv["days_late"] >= args.min_days:
            filtered.append(inv)
    overdue = filtered

    overdue.sort(key=lambda inv: inv["days_late"], reverse=True)
    

    print(f"OVERDUE INVOICES ({len(overdue)})")
    total = 0
    for inv in overdue:
        level = classify_overdue(inv["days_late"])
        print(f"{inv["invoice_no"]} | {inv["client"]:<12} | "
              f"${inv["amount"]:>9,.2f} | {inv["days_late"]:>3} days | {level} ")
        total += inv["amount"]
    print(f"\nTotal overdue: ${total:,.2f}")

    per_client = {}
    for inv in overdue:
        per_client[inv["client"]] = per_client.get(inv["client"], 0) + inv["amount"]
    print("\nOVERDUE PER CLIENT")
    for client, amount in sorted(per_client.items(), key=lambda p: p[1], reverse=True):
        print(f"{client:<12} ${amount:>10,.2f}")

    print(f"\nSKIPPED ROWS ({len(skipped)})")
    for line_no, invoice_no, reason in skipped:
        print(f"line {line_no} ({invoice_no}): {reason}")


if __name__ == "__main__":
    main()