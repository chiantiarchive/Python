import argparse
from datetime import date

from loader import load_invoices
from logic import classify_overdue, find_overdue
from memory import already_done, get_connection, mark_done


def parse_args():
    parser = argparse.ArgumentParser(description="Overdue invoice checker")
    parser.add_argument("--input", default="invoices.csv",
                        help="path to the invoice CSV")
    parser.add_argument("--min-days", type=int, default=1,
                        help="only show invoices at least this many days late")
    parser.add_argument("--dry-run", action="store_true",
                        help="show what would be reported, without recording anything")
    return parser.parse_args()


def main():
    args = parse_args()
    today = date.today()
    invoices, skipped = load_invoices(args.input)
    overdue = find_overdue(invoices, today)

    filtered = []
    for inv in overdue:
        if inv["days_late"] >= args.min_days:
            filtered.append(inv)

    connection = get_connection()
    try:
        fresh = []
        for inv in filtered:
            if not already_done(connection, inv["invoice_no"]):
                fresh.append(inv)
        fresh.sort(key=lambda inv: inv["days_late"], reverse=True)

        print(f"OVERDUE INVOICES ({len(fresh)})")
        total = 0 
        for inv in fresh:
            level = classify_overdue(inv["days_late"])
            print(f"{inv["invoice_no"]} | {inv["client"]} |"
                  f"${inv["amount"]:>9,.2f} | {inv["days_late"]:>3} days| {level}")
            total += inv["amount"]
        print(f"\nTotal overdue: ${total:,.2f}")

        per_client = {}
        for inv in fresh:
            per_client[inv["client"]] = per_client.get(inv["client"], 0) + inv["amount"]
        print("\nOVERDUE PER CLIENT")
        for client, amount in sorted(per_client.items(), key=lambda p: p[1], reverse=True):
            print(f"{client:<12} ${amount:>10,.2f}")

        print(f"\nSKIPPED ROWS ({len(skipped)})")
        for line_no, invoice_no, reason in skipped:
            print(f"line {line_no} ({invoice_no}): {reason}")

        if args.dry_run:
            print("\n[DRY RUN] NOTHING was recorded.")
        else:
            for inv in fresh:
                mark_done(connection, inv["invoice_no"], today.isoformat())
    finally:
        connection.close()


if __name__ == "__main__":
    main()