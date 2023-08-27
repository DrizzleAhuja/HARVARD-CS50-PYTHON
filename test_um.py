import pytest
from um import count

def test_count_um():
    assert count("hello, um, world") == 1
    assert count("um, um, um, um") == 4
    assert count("um is a placeholder") == 1
    assert count("Let's um, see um, how um it goes") == 3

def test_no_um():
    assert count("yummy") == 0
    assert count("Umbrella") == 0
    assert count("Something") == 0
