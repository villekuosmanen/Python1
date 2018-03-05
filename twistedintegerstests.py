import unittest
from twistedintegers import TwistedIntegers

class TwistedIntegers_Test(unittest.TestCase):

    # twisted integers (list) testing

    def test_zero_length(self):
        self.assertRaises(ValueError, TwistedIntegers, 0)

    def test_negative_length(self):
        self.assertRaises(ValueError, TwistedIntegers, -1)

    def test_regular_length(self):
        z = TwistedIntegers(5)
        self.assertEqual("[0, 1, 2, 3, 4]", str(z))

    def test_find_size(self):
        z = TwistedIntegers(5)
        self.assertEqual(5, TwistedIntegers.Size(z))
