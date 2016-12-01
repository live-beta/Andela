import unittest

from prime_number import is_prime

class TestCalculator(unittest.TestCase):
    def test_negative_numbers(self):
        self.assertEqual(prime_gen(-3),'Negatives not allowed')

    def test_range_numbers(self):
        range_size= number -2
        if range_size <= 0:
            print "no range can be computed"
    def test_string_inputs(self):
        self.assertEqual(prime_gen(str),'String inputs not valid')
    def test_decimal_inputs(self):
        self.assertEqual(prime_gen(1.1),'Decimal inputs are not allowed')
    def test_float_inputs(self):
        self.assertEqual(prime_gen(0.112),'Floating point inputs not allowed')
