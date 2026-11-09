def clean_phone(raw):
    digits = ""
    for ch in raw:
        if ch.isdigit():
            digits += ch
    return digits


def is_valid_phone(raw):
    return len(clean_phone(raw)) == 10


print(repr(clean_phone("(555) 123-4567")))   # '5551234567'
print(is_valid_phone("(555) 123-4567"))      # True

print(repr(clean_phone("")))                 # ''
print(is_valid_phone(""))                    # False

print(repr(clean_phone("abc")))              # ''
print(is_valid_phone("abc"))                 # False

print(repr(clean_phone("555-1234")))         # '5551234'
print(is_valid_phone("555-1234")) 