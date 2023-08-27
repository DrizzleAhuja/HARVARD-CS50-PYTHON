from bank import value

def test_value_hello():
    assert value("Hello, world!") == 0

def test_value_h():
    assert value("Hey there!") == 20

def test_value_other():
    assert value("What's up?") == 100

def test_value_case_insensitive():
    assert value("hola, amigos!") == 20

def test_value_empty():
    assert value("") == 100

# Run the tests if the script is executed directly
if __name__ == "__main__":
    import pytest
    pytest.main()
