import csv
import logging
from datetime import date
from pathlib import Path

from models import Invoice

logger = logging.getLogger(__name__)


def parse_row(row):
    client = row["client"].strip()
    if not client:
        raise ValueError("missing client")

    try:
        amount = float(row["amount"])
    except ValueError:
        raise ValueError(f"bad amount '{row["amount"]}'")

    try:
        due = date.fromisoformat(row["due_date"])
    except ValueError:
        raise ValueError(f"bad due date '{row["due_date"]}'")

    paid = row["paid"].strip().lower() == "yes"
    return Invoice(row["invoice_no"], client, amount, due, paid)


def load_invoices(path):
    good, skipped = [], []
    with Path(path).open("r", newline="", encoding="utf-8-sig") as f:
        for line_no, row in enumerate(csv.DictReader(f), start=2):
            try:
                good.append(parse_row(row))
            except (ValueError, KeyError) as error:
                invoice_no = row.get("invoice_no", "?")
                skipped.append((line_no, invoice_no, str(error)))
                logger.warning("Skipped line %d (%s): %s", line_no, invoice_no, error)
    logger.info("Loaded %d invoices, skipped %d", len(good), len(skipped))
    return good, skipped