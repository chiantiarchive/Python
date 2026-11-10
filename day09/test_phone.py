from phone import clean_phone, is_valid_phone


def test_clean_remove_symbols():
    assert clean_phone("(555) 123-4567") == "5551234567"


def test_empty_string():
    assert clean_phone("") == ""


def test_country_code_is_kept():
    assert clean_phone("+63 912 345 6789") == "639123456789"