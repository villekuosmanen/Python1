import unittest
from twistedintegers import TwistedIntegers
from twistedmatrix import TwistedMatrix

class TwistedIntegers_Test(unittest.TestCase):

    # twisted integers (list) testing

    def test_diff_length(self):
        x = TwistedIntegers(3)
        y = TwistedIntegers(5)
        self.assertRaises(ValueError, TwistedMatrix.__init__, self, [x,y])

    def test_same_length(self):
        x = TwistedIntegers(2)
        y = TwistedIntegers(2)
        m = TwistedMatrix([x,y])
        self.assertEqual("[\"[\'<0:2>\', \'<1:2>\']\", \"[\'<0:2>\', \'<1:2>\']\"]", str(m))    
