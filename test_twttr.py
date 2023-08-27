from twttr import shorten

def test_shorten_no_vowels():
    assert shorten("hello") == "hll"

def test_shorten_with_vowels():
    assert shorten("programming") == "prgrmmng"

def test_shorten_mixed_case():
    assert shorten("Ecstatic") == "csttc"

def test_shorten_empty_string():
    assert shorten("") == ""

def test_shorten_only_vowels():
    assert shorten("aeiouAEIOU") == ""

# Run the tests if the script is executed directly
if __name__ == "__main__":
    import pytest
    pytest.main()
