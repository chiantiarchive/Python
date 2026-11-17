from datetime import date

import openpyxl

from models import Invoice
from report import build_report

TODAY = date(2026, 11, 10)


def sample():
    return [
        Invoice("INV-1", "Chianti", 100.0, date(2026, 11, 1)),
        Invoice("INV-2", "Serene", 250.5, date(2026, 10,1)),
        Invoice("INV-3", "Chianti", 50.0, date(2026, 10, 20)),
    ]


def test_report_has_two_sheets(tmp_path):
    path = build_report(sample(), TODAY, tmp_path / "r.xlsx")
    assert openpyxl.load_workbook(path).sheetnames == ['Summary', 'Data']


def test_summary_is_sorted_with_total_row(tmp_path):
    path = build_report(sample(), TODAY, tmp_path / "r.xlsx")
    ws = openpyxl.load_workbook(path)["Summary"]
    assert [ws["A2"].value, ws["A3"].value] == ["Serene", "Chianti"]
    assert [cell.value for cell in ws[ws.max_row]] == ["TOTAL", 400.5]


def test_data_sheet_has_every_invoice(tmp_path):
    path = build_report(sample(), TODAY, tmp_path / "r.xlsx")
    ws = openpyxl.load_workbook(path)["Data"]
    assert ws.max_row == 4


def test_headers_frozen_and_money_formatted(tmp_path):
    path = build_report(sample(), TODAY, tmp_path / "r.xlsx")
    wb = openpyxl.load_workbook(path)
    assert wb["Summary"].freeze_panes == "A2"
    assert wb["Data"].freeze_panes == "A2"
    assert wb["Summary"]["B2"].number_format == "#,##0.00"