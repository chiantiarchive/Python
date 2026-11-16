from datetime import date

import pandas as pd

today = pd.Timestamp(date.today())

df = pd.read_csv("invoices.csv")
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
df["due_date"] = pd.to_datetime(df["due_date"], format="%Y-%m-%d",
                                errors ="coerce")
df["client"] = df["client"].fillna("").str.strip()
df = df[df["client"] != ""]
df = df.dropna(subset=["amount", "due_date"])
df["paid"] = df["paid"].str.strip().str.lower() == "yes"
df["days_late"] = (today - df["due_date"]).dt.days

overdue = df[(~df["paid"]) & (df["days_late"] > 0)]
summary = overdue.groupby("client")["amount"].sum().sort_values(ascending=False)


print(summary.round(2))
print("Total:", round(overdue["amount"].sum(), 2))
print("Rows:", len(overdue))