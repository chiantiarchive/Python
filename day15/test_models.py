from datetime import date

import pytest

from loader import parse_row
from logic import find_overdue, totals_by_client
from models import Invoice

TODAY = date(2026, 11, 10)


def test_days_overdue():
    inv = Invoice("INV-1", "Chianti", 100.0, date(2026, 11, 1))
    assert inv.days_overdue(TODAY) == 9   


def test_paid_invoice_is_not_overdue():
    inv = Invoice("INV-1","Chianti", 100.0, date(2026, 12, 1))
    assert find_overdue([inv], TODAY) == []


def test_totals_by_client_sorted_high_to_low():
    invoices = [
        Invoice("1", "Chianti", 50.0, date(2026, 1, 1)),
        Invoice("2", "Serene", 200.0, date(2026, 1, 1)),
        Invoice("3", "Chianti", 100.0, date(2026, 1, 1)),
    ]
    totals = totals_by_client(invoices)
    assert totals == {"Serene": 200.0, "Chianti": 150.0}
    assert list(totals) == ["Serene", "Chianti"]


def test_parse_row_returns_invoice():
    row = {"invoice_no": "INV-1", "client": "Chianti", "amount": "100.5",
           "due_date": "2026-11-01", "paid": "No"}
    inv = parse_row(row)
    assert isinstance(inv, Invoice)
    assert inv.client == "Chianti"
    assert inv.amount == 100.5
    assert inv.paid is False


def test_parse_row_rejects_missing_client():
    row = {"invoice_no": "INV-1", "client": "", "amount": "10",
           "due_date": "2026-11-01", "paid": "no"}
    with pytest.raises(ValueError):
        parse_row(row)