import pytest
from working import convert

def test_valid_time_formats():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"

def test_invalid_time_formats():
    with pytest.raises(ValueError):
        convert("9:00 to 5:00 PM")

    with pytest.raises(ValueError):
        convert("9:00 AM to 5:00")

    with pytest.raises(ValueError):
        convert("9:00 AM 5:00 PM")

    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")

    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")

    with pytest.raises(ValueError):
        convert("9:00 AM to 13:00 PM")
