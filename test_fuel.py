import pytest
from fuel import convert, gauge

# Test convert function
def test_convert_valid_fraction():
    assert convert("50/100") == 50

def test_convert_invalid_fraction():
    with pytest.raises(ValueError):
        convert("abc/100")
    with pytest.raises(ValueError):
        convert("50/abc")
    with pytest.raises(ValueError):
        convert("50/100/200")
    with pytest.raises(ValueError):
        convert("100/50")

def test_convert_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        convert("50/0")

# Test gauge function
def test_gauge_E():
    assert gauge(1) == "E"
    assert gauge(0) == "E"

def test_gauge_F():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_gauge_percentage():
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"
    assert gauge(75) == "75%"

if __name__ == "__main__":
    pytest.main()
