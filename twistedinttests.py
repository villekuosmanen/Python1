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

    # twisted integers (list) testing

    def test_zero_length(self):
        self.assertRaises(ValueError, TwistedIntegers.__init__, self, 0)

    def test_negative_length(self):
        self.assertRaises(ValueError, TwistedIntegers.__init__, self, -1)

    def test_regular_length(self):
        z = TwistedIntegers(5)
        self.assertEqual("[0, 1, 2, 3, 4]", str(z))

    def test_find_size(self):
        z = TwistedIntegers(5)
        self.assertEqual(5, TwistedIntegers.Size(z))

    #tests for the functions that check properties of twisted integers

    def test_addComm_isValid(self):
        #Proven that this will be true for all n
        self.assertTrue(TwistedInt.isAddCommutative(5))

    def test_addComm_zeronN(self):
        self.assertRaises(ValueError, TwistedInt.isAddCommutative, 0)

    def test_mulComm_isValid(self):
        #Proven that this will be true for all n
        self.assertTrue(TwistedInt.isMulCommutative(5))

    def test_mulComm_zeronN(self):
        self.assertRaises(ValueError, TwistedInt.isMulCommutative, 0)

    def test_addAss_isValid(self):
        #Proven that this will be true for all n
        self.assertTrue(TwistedInt.isAddAssociative(5))

    def test_addAss_zeronN(self):
        self.assertRaises(ValueError, TwistedInt.isAddAssociative, 0)

    #TODO Test the validity of MulAss

    def test_isMulAss_valid(self): # RECHECK!
        self.assertTrue(TwistedInt.isMulAssociative(100))

    def test_mulAss_zeronN(self):
        self.assertRaises(ValueError, TwistedInt.isMulAssociative, 0)

    #TODO Test the validity of Dist

    def test_isDistr_valid(self):
        self.assertFalse(TwistedInt.isDistributive(100))

    def test_isDistr_zeronN(self):
        self.assertRaises(ValueError, TwistedInt.isDistributive, 0)
