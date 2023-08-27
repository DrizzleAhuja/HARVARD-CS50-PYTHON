import unittest
from datetime import date
from seasons import calculate_age_in_minutes, convert_to_words

class TestSeasons(unittest.TestCase):

    def test_calculate_age_in_minutes(self):
        birth_date = date(2000, 1, 1)
        current_date = date(2023, 8, 25)
        expected_age_in_minutes = (current_date - birth_date).days * 24 * 60
        calculated_age_in_minutes = calculate_age_in_minutes(birth_date)
        self.assertEqual(expected_age_in_minutes, calculated_age_in_minutes)

    def test_convert_to_words(self):
        self.assertEqual(convert_to_words(1), "one minute")
        self.assertEqual(convert_to_words(15), "fifteen minutes")
        self.assertEqual(convert_to_words(20), "twenty minutes")
        self.assertEqual(convert_to_words(21), "twenty-one minutes")
        self.assertEqual(convert_to_words(55), "fifty-five minutes")
        self.assertEqual(convert_to_words(60), "one hour minutes")  # Just for demonstration

if __name__ == '__main__':
    unittest.main()
