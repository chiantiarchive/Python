from pathlib import Path

import openpyxl
from openpyxl.styles import Font, PatternFill

from logic import classify_overdue, totals_by_client

HEADER_FONT = Font(bold=True, color="FFFFFF")
HEADER_FILL = PatternFill("solid", start_color="1F4E78")
MONEY = "#,##0.00"


def style_header(ws):
    for cell in ws[1]:
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL
    ws.freeze_panes = "A2"


def build_report(invoices, today, path):
    wb = openpyxl.Workbook()

    summary = wb.active
    summary.title = "Summary"
    summary.append(["Client", "Total overdue"])
    grand_total = 0
    for client, amount in totals_by_client(invoices).items():
        summary.append([client, round(amount, 2)])
        grand_total += amount
    summary.append(["TOTAL",  round(grand_total, 2)])
    for cell in summary[summary.max_row]:
        cell.font = Font(bold=True)
    for row in summary.iter_rows(min_row=2, min_col=2, max_col=2):
        row[0].number_format = MONEY
    style_header(summary)
    summary.column_dimensions["A"].width = 24
    summary.column_dimensions["B"].width = 18

    data =wb.create_sheet("Data")
    data.append(["Invoice","Client", "Amount", "Due date", "Days late", "Level"])
    for inv in invoices:
        days = inv.days_overdue(today)
        data.append([inv.invoice_no, inv.client, inv.amount, inv.due,
                    days, classify_overdue(days)])
    for row in data.iter_rows(min_row=2, min_col=3, max_col=3):
        row[0].number_format = MONEY
    for row in data.iter_rows(min_row=2, min_col=4, max_col=4):
        row[0].number_format = "yyyy-mm-dd"
    style_header(data)
    for letter, width in zip("ABCDEF", (12, 20, 14, 13 ,11, 20)):
        data.column_dimensions[letter].width = width

    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    wb.save(path)
    return path