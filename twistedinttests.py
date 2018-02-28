import unittest
from twistedints import TwistedInt

class TwistedInt_Test(unittest.TestCase):

    def test_init_valid(self):
        a = TwistedInt(2,5)
        self.assertEqual(2, a.value)
        self.assertEqual(5, a.n)

    def test_init_nAndValueEqual(self):
        a = TwistedInt(2,2)
        self.assertEqual(2, a.value)
        self.assertEqual(2, a.n)

    def test_init_zeroValue(self):
        a = TwistedInt(0,8)
        self.assertEqual(0, a.value)
        self.assertEqual(8, a.n)

    def test_init_negativeN(self):
        self.assertRaises(ValueError, TwistedInt.__init__, self, 2, -1)

    def test_init_nSmallerThanValue(self):
        self.assertRaises(ValueError, TwistedInt.__init__, self, 7, 6)

    def test_init_negativeValue(self):
        self.assertRaises(ValueError, TwistedInt.__init__, self, -3, 1)

    def test_str_correctFormat(self):
        a = TwistedInt(2,5)
        self.assertEqual("<2:5>", str(a))