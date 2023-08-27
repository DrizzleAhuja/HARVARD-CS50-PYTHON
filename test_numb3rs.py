from numb3rs import validate


def test_valid_ipv4():
    assert validate("192.168.1.1") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("10.0.0.1") == True


def test_invalid_ipv4():
    assert validate("275.3.6.28") == False
    assert validate("192.168.256.1") == False
    assert validate("10.0.0.01") == False
    assert validate("1.2.3") == False
    assert validate("hello.world.123") == False
    assert validate("256.256.256.256") == False


def test_malformed_ipv4():
    assert validate("192.168.1") == False
    assert validate("192.168.1.1.1") == False
    assert validate(".192.168.1.1") == False
    assert validate("192..168.1.1") == False
