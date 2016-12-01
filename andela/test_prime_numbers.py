import unittest

from prime_number import is_prime

class TestCalculator(unittest.TestCase):
    def test_negative_numbers(self):
        self.assertEqual(is_prime(-3),'Negatives not allowed')
    
