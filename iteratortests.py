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
