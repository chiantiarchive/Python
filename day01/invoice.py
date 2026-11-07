name = input("Client name: ").strip().title()
hours = float(input("Hours worked: "))
rate = float(input("Hourly rate: "))
total = round(hours * rate, 2)

print(f"{name} | {hours:,.1f} hrs x ${rate:,.2f} = ${total:,.2f}")
print(type(hours), type(name))