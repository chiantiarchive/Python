import pytest
from logic import classify_overdue

@pytest.mark.parametrize("days, expected", [
    (0, "On time"),
    (1, "Friendly reminder"),
    (14, "Friendly reminder"),
    (15, "Firm reminder"),
    (31, "Escalate"),
])
def test_classify_overdue(days, expected):
    assert classify_overdue(days) == expected