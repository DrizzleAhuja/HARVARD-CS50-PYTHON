import unittest
from jar import Jar

class TestJar(unittest.TestCase):

    def test_initial_capacity(self):
        jar = Jar()
        self.assertEqual(jar.capacity, 12)

    def test_custom_capacity(self):
        jar = Jar(20)
        self.assertEqual(jar.capacity, 20)

    def test_invalid_capacity(self):
        with self.assertRaises(ValueError):
            Jar(-5)

    def test_deposit(self):
        jar = Jar()
        jar.deposit(3)
        self.assertEqual(jar.size, 3)

    def test_withdraw(self):
        jar = Jar()
        jar.deposit(5)
        jar.withdraw(2)
        self.assertEqual(jar.size, 3)

    def test_withdraw_more_than_available(self):
        jar = Jar()
        jar.deposit(3)
        with self.assertRaises(ValueError):
            jar.withdraw(5)

    def test_deposit_beyond_capacity(self):
        jar = Jar(4)
        with self.assertRaises(ValueError):
            jar.deposit(5)

    def test_invalid_deposit(self):
        jar = Jar()
        with self.assertRaises(ValueError):
            jar.deposit(-2)

    def test_invalid_withdraw(self):
        jar = Jar()
        with self.assertRaises(ValueError):
            jar.withdraw(-1)

    def test_str_representation(self):
        jar = Jar()
        jar.deposit(5)
        self.assertEqual(str(jar), "🍪🍪🍪🍪🍪")

if __name__ == '__main__':
    unittest.main()
