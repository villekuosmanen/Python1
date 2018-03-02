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

    def test_add2(self):
        x = [TwistedInt(1,9), TwistedInt(2,9)]
        y = [TwistedInt(3,9), TwistedInt(4,9)]
        x1 = [TwistedInt(5,9), TwistedInt(6,9)]
        y1 = [TwistedInt(7,9), TwistedInt(8,9)]
        m1 = TwistedMatrix([x,y])
        m2 = TwistedMatrix([x1,y1])
        self.assertEqual("[\"[\'<8:9>\', \'<1:9>\']\", \"[\'<0:9>\', \'<6:9>\']\"]", str(m1+m2))

    def test_mul(self):
        x = [TwistedInt(1,9), TwistedInt(2,9)]
        y = [TwistedInt(3,9), TwistedInt(4,9)]
        x1 = [TwistedInt(5,9), TwistedInt(6,9)]
        y1 = [TwistedInt(7,9), TwistedInt(8,9)]
        m1 = TwistedMatrix([x,y])
        m2 = TwistedMatrix([x1,y1])
        self.assertEqual("[\"[\'<7:9>\', \'<3:9>\']\", \"[\'<8:9>\', \'<8:9>\']\"]", str(m1*m2))    
