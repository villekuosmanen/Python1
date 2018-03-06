import unittest
from twistedintegers import TwistedIntegers

class TwistedIntegers_Test(unittest.TestCase):

    # twisted integers (list) testing

    def test_zero_length(self):
        """Tests creation of TwistedIntegers object with n = 0"""
        self.assertRaises(ValueError, TwistedIntegers, 0)

    def test_negative_length(self):
        """Tests creation of TwistedIntegers object with n < 0"""
        self.assertRaises(ValueError, TwistedIntegers, -1)

    def test_regular_length(self):
        """Tests the base case of creating a TwistedIntegers object"""
        z = TwistedIntegers(5)
        self.assertEqual("['<0:5>', '<1:5>', '<2:5>', '<3:5>', '<4:5>']", str(z))

    def test_find_size(self):
        """Tests finding the size of TwistedIntegers"""
        z = TwistedIntegers(5)
        self.assertEqual(5, TwistedIntegers.Size(z))
