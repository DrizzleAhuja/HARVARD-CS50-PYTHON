import plates

def test_valid_plates():
    assert plates.is_valid("ABC123")
    assert plates.is_valid("XYZ789")
    assert plates.is_valid("123XYZ")

def test_invalid_plates():
    assert not plates.is_valid("INVALID")
    assert not plates.is_valid("ABC 123")
    assert not plates.is_valid("ABCD")
    assert not plates.is_valid("1234567")

def test_edge_cases():
    assert not plates.is_valid("")
    assert not plates.is_valid("A")
    assert not plates.is_valid("ABC1234")
    assert not plates.is_valid("1 2 3")

def test_zero_placement():
    assert not plates.is_valid("ABC012")
    assert not plates.is_valid("XYZ007")

def test_alphanumeric_check():
    assert not plates.is_valid("ABC1@3")
    assert not plates.is_valid("XY#789")

# Run all test functions
if __name__ == "__main__":
    import pytest
    pytest.main(["-v", "test_plates.py"])

