import unittest
from twistedints import TwistedInt
from twistedintegers import TwistedIntegers

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

    # addition testing
    def test_add_valid(self):
        a = TwistedInt(2,5)
        b = TwistedInt(4,5)
        self.assertEqual("<1:5>", str(a+b))

    def test_add_sameValue(self):
        a = TwistedInt(2,5)
        self.assertEqual("<4:5>", str(a+a))

    def test_add_equalValues(self):
        a = TwistedInt(2,5)
        b = TwistedInt(2,5)
        self.assertEqual("<4:5>", str(a+b))

    def test_add_zeroValue(self):
        a = TwistedInt(2,5)
        b = TwistedInt(0,5)
        self.assertEqual("<2:5>", str(a+b))

    def test_add_differentN(self):
        a = TwistedInt(2,5)
        b = TwistedInt(0,2)
        self.assertRaises(ValueError, TwistedInt.__add__, a, b)

    # multiplication testing
    def test_mul_valid(self):
        a = TwistedInt(2,5)
        b = TwistedInt(4,5)
        self.assertEqual("<4:5>", str(a*b))

    def test_mul_sameValue(self):
        a = TwistedInt(3,5)
        self.assertEqual("<0:5>", str(a*a))

    def test_mul_equalValues(self):
        a = TwistedInt(3,5)
        b = TwistedInt(3,5)
        self.assertEqual("<0:5>", str(a*b))

    def test_mul_zeroValue(self):
        a = TwistedInt(2,5)
        b = TwistedInt(0,5)
        self.assertEqual("<2:5>", str(a*b))

    def test_mul_differentN(self):
        a = TwistedInt(2,5)
        b = TwistedInt(0,2)
        self.assertRaises(ValueError, TwistedInt.__mul__, a, b)
