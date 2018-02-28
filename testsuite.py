import unittest
import sys
from twistedinttests import TwistedInt_Test

def suite():
    loader = unittest.TestLoader()
    testSuite = loader.loadTestsFromTestCase(TwistedInt_Test)
    return testSuite

def test():
    testSuite = suite()
    runner = unittest.TextTestRunner(sys.stdout, verbosity=2)
    result = runner.run(testSuite)

test()