# start with nothing collected
# look at each character, one at a time
# if it's a digit, keep it
# give back what I kept


def clean_phone(raw):
    """Return only the digit from a phone number string."""
    digits = ""
    for ch in raw:
        if ch.isdigit():
            digits += ch
    return digits


def is_valid_phone(raw):
    """Return True only if the number has exactly 10 digit."""
    return len(clean_phone(raw)) == 10


# Tests
print(repr(clean_phone("(555) 123-4567")))   # '5551234567'
print(is_valid_phone("(555) 123-4567"))      # True

print(repr(clean_phone("")))                 # ''
print(is_valid_phone(""))                    # False

print(repr(clean_phone("abc")))              # ''
print(is_valid_phone("abc"))                 # False

print(repr(clean_phone("555-1234")))         # '5551234'
print(is_valid_phone("555-1234"))            # False