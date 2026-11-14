import argparse
from datetime import date

from loader import load_invoices
from logic import classify_overdue, find_overdue, totals_by_client
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
    late_enough = [inv for inv in overdue if inv.days_overdue(today) >= args.min_days]

    connection = get_connection()
    try:
        fresh = [inv for inv in late_enough
                 if not already_done(connection, inv.invoice_no)]
        fresh.sort(key=lambda inv: inv.days_overdue(today), reverse=True)

        print(f"OVERDUE INVOICES ({len(fresh)})")
        for inv in fresh:
            days = inv.days_overdue(today)
            level = classify_overdue(days)
            print(f"{inv.invoice_no} | {inv.client:<12} | "
                  f"${inv.amount:>9,.2f} | {days:>3} days | {level}")
        total = sum(inv.amount for inv in fresh)
        print(f"\nTotal overdue: ${total}")

        print(f"\nOVERDUE PER CLIENT")
        for client, amount in totals_by_client(fresh).items():
            print(f"{client:<12} ${amount:<10,.2f}")

        print(f"SKIPPED ROWS ({len(skipped)})")
        for line_no, invoice_no, reason in skipped:
            print(f"line {line_no} ({invoice_no}):{reason}")

        if args.dry_run:
            print("\n{DRY RUN} Nothing was recorded.")
        else:
            for inv in fresh:
                mark_done(connection, inv.invoice_no, today.isoformat())
    finally:
        connection.close()


if __name__ == "__main__":
    main()