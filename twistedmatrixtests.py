import unittest
from twistedints import TwistedInt
from twistedmatrix import TwistedMatrix

class TwistedIntegers_Test(unittest.TestCase):

    # twisted integers (list) testing

    def test_diff_length(self):
        x = [TwistedInt(0,2), TwistedInt(1,2)]
        y = [TwistedInt(0,3), TwistedInt(1,3), TwistedInt(2,3)]
        self.assertRaises(ValueError, TwistedMatrix.__init__, self, [x,y])

    def test_same_length(self):
        x = [TwistedInt(0,2), TwistedInt(1,2)]
        y = [TwistedInt(0,2), TwistedInt(1,2)]
        m = TwistedMatrix([x,y])
        self.assertEqual("[\"[\'<0:2>\', \'<1:2>\']\", \"[\'<0:2>\', \'<1:2>\']\"]", str(m))

    def test_add(self):
        x = [TwistedInt(0,2), TwistedInt(1,2)]
        y = [TwistedInt(0,2), TwistedInt(1,2)]
        m1 = TwistedMatrix([x,y])
        m2 = TwistedMatrix([x,y])
        self.assertEqual("[\"[\'<0:2>\', \'<0:2>\']\", \"[\'<0:2>\', \'<0:2>\']\"]", str(m1+m2))
