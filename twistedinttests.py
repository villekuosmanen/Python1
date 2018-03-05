import unittest
from twistedints import TwistedInt
from twistedintegers import TwistedIntegers

class TwistedInt_Test(unittest.TestCase):

    def test_init_valid(self):
        """Tests a normal case of Twisted Int creation"""
        a = TwistedInt(2,5)
        self.assertEqual(2, a.value)
        self.assertEqual(5, a.n)

    def test_init_nAndValueEqual(self):
        """Tests an initialization where the n and value are equal"""
        a = TwistedInt(2,2)
        self.assertEqual(2, a.value)
        self.assertEqual(2, a.n)

    def test_init_zeroValue(self):
        """Tests an initialization where the value is zero"""
        a = TwistedInt(0,8)
        self.assertEqual(0, a.value)
        self.assertEqual(8, a.n)

    def test_init_negativeN(self):
        """Tests that initializing n to be negative throws an error"""
        self.assertRaises(ValueError, TwistedInt, 2, -1)

    def test_init_nSmallerThanValue(self):
        """Tests that initializing n to be smaller than the value throws an error"""
        self.assertRaises(ValueError, TwistedInt, 7, 6)

    def test_init_negativeValue(self):
        """Tests that initializing the value to be negative throws an error"""
        self.assertRaises(ValueError, TwistedInt, -3, 1)

    def test_str_correctFormat(self):
        """Tests the formatting of the toString fuction of Twisted Ints"""
        a = TwistedInt(2,5)
        self.assertEqual("<2:5>", str(a))

    # addition testing
    def test_add_validModuloCalled(self):
        """Tests adding two twisted ints together where the result gets trunctuated by the mod n function"""
        a = TwistedInt(2,5)
        b = TwistedInt(4,5)
        self.assertEqual("<1:5>", str(a+b))

    # addition testing
    def test_add_validModuloNotCalled(self):
        """Tests adding two twisted ints together where the two values\' sum is smaller than n"""
        a = TwistedInt(2,5)
        b = TwistedInt(1,5)
        self.assertEqual("<3:5>", str(a+b))

    def test_add_sameValue(self):
        """Tests adding the same twisted int together with itself"""
        a = TwistedInt(2,5)
        self.assertEqual("<4:5>", str(a+a))

    def test_add_equalValues(self):
        """Tests adding two twisted ints that have the same value"""
        a = TwistedInt(2,5)
        b = TwistedInt(2,5)
        self.assertEqual("<4:5>", str(a+b))

    def test_add_zeroValue(self):
        """Tests adding a twisted int with a valid twisted int of value 0"""
        a = TwistedInt(2,5)
        b = TwistedInt(0,5)
        self.assertEqual("<2:5>", str(a+b))

    def test_add_differentN(self):
        """Tests that adding twisted ints that have a different n throws an error"""
        a = TwistedInt(2,5)
        b = TwistedInt(0,2)
        self.assertRaises(ValueError, TwistedInt.__add__, a, b)

    # multiplication testing
    def test_mul_validModuloCalled(self):
        """Tests multiplying two twisted ints together where the result gets trunctuated by the mod n function"""
        a = TwistedInt(2,5)
        b = TwistedInt(4,5)
        self.assertEqual("<4:5>", str(a*b))

    # multiplication testing
    def test_mul_validModuloNotCalled(self):
        """Tests multiplying two twisted ints together where the result does not get trunctuated by the mod n function"""
        a = TwistedInt(1,5)
        b = TwistedInt(1,5)
        self.assertEqual("<3:5>", str(a*b))

    def test_mul_sameValue(self):
        """Tests multiplying the same twisted int together with itself"""
        a = TwistedInt(3,5)
        self.assertEqual("<0:5>", str(a*a))

    def test_mul_equalValues(self):
        """Tests multiplying two twisted ints that have the same value"""
        a = TwistedInt(3,5)
        b = TwistedInt(3,5)
        self.assertEqual("<0:5>", str(a*b))

    def test_mul_zeroValue(self):
        """Tests multiplying a twisted int with a valid twisted int of value 0"""
        a = TwistedInt(2,5)
        b = TwistedInt(0,5)
        self.assertEqual("<2:5>", str(a*b))

    def test_mul_differentN(self):
        """Tests that multiplying twisted ints that have a different n throws an error"""
        a = TwistedInt(2,5)
        b = TwistedInt(0,2)
        self.assertRaises(ValueError, TwistedInt.__mul__, a, b)

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

    #tests for the functions that check properties of twisted integers

    def test_addComm_isValid(self):
        """Tests that addition is commutative for n=5"""
        self.assertTrue(TwistedInt.isAddCommutative(5))

    def test_addComm_cornerCase(self):
        """Tests if testing for commutative addition works for n=1"""
        self.assertTrue(TwistedInt.isAddCommutative(1))

    def test_addComm_zeronN(self):
        """Tests that calling the test with n=0 throws an error"""
        self.assertRaises(ValueError, TwistedInt.isAddCommutative, 0)

    def test_mulComm_isValid(self):
        """Tests that multiplication is commutative for n=5"""
        self.assertTrue(TwistedInt.isMulCommutative(5))

    def test_mulComm_cornerCase(self):
        """Tests if testing for commutative multiplication works for n=1"""
        self.assertTrue(TwistedInt.isMulCommutative(1))

    def test_mulComm_zeronN(self):
        """Tests that calling the test with n=0 throws an error"""
        self.assertRaises(ValueError, TwistedInt.isMulCommutative, 0)

    def test_addAss_isValid(self):
        """Tests that addition is associative for n=5"""
        self.assertTrue(TwistedInt.isAddAssociative(5))

    def test_addAss_cornerCase(self):
        """Tests if testing for associative addition works for n=1"""
        self.assertTrue(TwistedInt.isAddAssociative(1))

    def test_addAss_zeronN(self):
        """Tests that calling the test with n=0 throws an error"""
        self.assertRaises(ValueError, TwistedInt.isAddAssociative, 0)

    def test_mulAss_valid(self):
        """Tests that multiplication is associative for n=5"""
        self.assertTrue(TwistedInt.isMulAssociative(4))

    def test_mulAss_cornerCase(self):
        """Tests if testing for associative multiplication works for n=1"""
        self.assertTrue(TwistedInt.isMulAssociative(1))

    def test_mulAss_zeronN(self):
        """Tests that calling the test with n=0 throws an error"""
        self.assertRaises(ValueError, TwistedInt.isMulAssociative, 0)

    #TODO Test the validity of Dist

    def test_isDistr_false(self):
        """Tests that twisted int arithmetic is not distributive for n=20"""
        self.assertFalse(TwistedInt.isDistributive(20))

    def test_isDistr_falseCornerCase(self):
        """Tests that twisted int arithmetic is not distributive for n=2"""
        self.assertFalse(TwistedInt.isDistributive(2))

    def test_isDistr_trueCornerCase(self):
        """Tests that twisted int arithmetic is distributive for n=1 and that the test works"""
        self.assertTrue(TwistedInt.isDistributive(1))

    def test_isDistr_zeronN(self):
        """Tests that calling the test with n=0 throws an error"""
        self.assertRaises(ValueError, TwistedInt.isDistributive, 0)
