import unittest
import sys
import os
from twistedinttests import TwistedInt_Test
from twistedintegerstests import TwistedIntegers_Test

def suite():
    loader = unittest.TestLoader()
    tests = []
    for filename in os.listdir(os.path.abspath(os.path.dirname(__file__))):
        if filename.endswith('tests.py'):
            tests.append(filename[:-3])
    testSuite = loader.loadTestsFromNames(tests)
    return testSuite

def test():
    testSuite = suite()
    runner = unittest.TextTestRunner(sys.stdout, verbosity=2)
    result = runner.run(testSuite)

test()
