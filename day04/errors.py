

raw_values = ["10", "abc", "7.5", ""]
good, failed = [], []

for raw in raw_values:
    try:
        good.append(float(raw))
    except ValueError as error:
        failed.append((raw, str(error)))

print("Good:", good)
print("Failed:", failed)


