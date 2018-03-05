import unittest
from twistedintegers import TwistedIntegers
from iterator import IteratorOfTwistedIntegers

class TwistedIntegersIterator_Test(unittest.TestCase):

    # twisted integers (list) testing

    def test_iteration(self):
        x = IteratorOfTwistedIntegers(TwistedIntegers(3))
        j = 0
        for i in x:
            self.assertEqual("<"+str(j)+":3>", str(i))
            j += 1

    # iterator addition testing

    def test_iteration_addValidOne(self):
        self.assertEqual(['<0:1>'], IteratorOfTwistedIntegers.addition(1))

    def test_iteration_addValidFive(self):
        self.assertEqual(['<0:5>'], IteratorOfTwistedIntegers.addition(5))

    def test_iteration_addValidTwenty(self):
        self.assertEqual(['<0:20>'], IteratorOfTwistedIntegers.addition(20))

    def test_iteration_addValidFortyTwo(self):
        self.assertEqual(['<0:42>'], IteratorOfTwistedIntegers.addition(42))

    def test_iteration_addValidHundred(self):
        self.assertEqual(['<0:100>'], IteratorOfTwistedIntegers.addition(100))

    def test_iteration_addZero(self):
        self.assertRaises(ValueError, IteratorOfTwistedIntegers.addition, 0)

    def test_iteration_addNegativeN(self):
        self.assertRaises(ValueError, IteratorOfTwistedIntegers.addition, -2)

    # iterator multiplication testing

    def test_iteration_mulValidOne(self):
        self.assertEqual(['<0:1>'], IteratorOfTwistedIntegers.multiplication(1))

    def test_iteration_mulValidFive(self):
        self.assertEqual(['<0:5>'], IteratorOfTwistedIntegers.multiplication(5))

    def test_iteration_mulValidTwenty(self):
        self.assertEqual(['<0:20>'], IteratorOfTwistedIntegers.multiplication(20))

    def test_iteration_mulValidFortyTwo(self):
        self.assertEqual(['<0:42>'], IteratorOfTwistedIntegers.multiplication(42))

    def test_iteration_mulValidHundred(self):
        self.assertEqual(['<0:100>'], IteratorOfTwistedIntegers.multiplication(100))

    def test_iteration_mulZero(self):
        self.assertRaises(ValueError, IteratorOfTwistedIntegers.multiplication, 0)

    def test_iteration_mulNegativeN(self):
        self.assertRaises(ValueError, IteratorOfTwistedIntegers.multiplication, -2)
