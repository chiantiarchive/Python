import sqlite3

DB_PATH = "app.db"


def get_connection(path=DB_PATH):
    connection = sqlite3.connect(path)
    with connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS processed_invoices (
                invoice_no TEXT PRIMARY KEY,
                processed_on TEXT
            )""")
    return connection


def already_done(connection, invoice_no):
    row = connection.execute(
        "SELECT 1 FROM processed_invoices WHERE invoice_no = ?", (invoice_no,)
    ).fetchone()
    return row is not None


def mark_done(connection, invoice_no, when):
    with connection:
        connection.execute(
            "INSERT OR IGNORE INTO processed_invoices VALUES (?, ?)",
            (invoice_no, when),
        )


if __name__ == "__main__":
    con = get_connection(":memory:")
    print(already_done(con, "INV-001"))
    mark_done(con, "INV-001", "2026-10-27")
    print(already_done(con, "INV-001"))
    con.close()