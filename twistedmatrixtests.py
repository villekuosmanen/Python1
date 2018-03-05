import unittest
from twistedints import TwistedInt
from twistedmatrix import TwistedMatrix

class TwistedMatrices_Test(unittest.TestCase):

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
        self.assertEqual("[\"[\'<6:9>\', \'<8:9>\']\", \"[\'<1:9>\', \'<3:9>\']\"]", str(m1+m2))

    def test_add_wrong_dimensions(self):
        x = [TwistedInt(1,11), TwistedInt(2,11)]
        y = [TwistedInt(3,11), TwistedInt(4,11)]
        z = [TwistedInt(5,11), TwistedInt(6,11)]
        x1 = [TwistedInt(7,11), TwistedInt(8,11)]
        y1 = [TwistedInt(9,11), TwistedInt(10,11)]
        m1 = TwistedMatrix([x,y,z])
        m2 = TwistedMatrix([x1,y1])
        self.assertRaises(ValueError, TwistedMatrix.__add__, m2,m1)

    def test_mul(self):
        x = [TwistedInt(1,9), TwistedInt(2,9)]
        y = [TwistedInt(3,9), TwistedInt(4,9)]
        x1 = [TwistedInt(5,9), TwistedInt(6,9)]
        y1 = [TwistedInt(7,9), TwistedInt(8,9)]
        m1 = TwistedMatrix([x,y])
        m2 = TwistedMatrix([x1,y1])
        self.assertEqual("[\"[\'<7:9>\', \'<3:9>\']\", \"[\'<8:9>\', \'<8:9>\']\"]", str(m1*m2))

    def test_mul_diff_dimensions(self):
        x = [TwistedInt(1,11), TwistedInt(2,11)]
        y = [TwistedInt(3,11), TwistedInt(4,11)]
        z = [TwistedInt(5,11), TwistedInt(6,11)]
        x1 = [TwistedInt(7,11), TwistedInt(8,11)]
        y1 = [TwistedInt(9,11), TwistedInt(10,11)]
        m1 = TwistedMatrix([x,y,z])
        m2 = TwistedMatrix([x1,y1])
        self.assertEqual("[\"[\'<0:11>\', \'<5:11>\']\", \"[\'<3:11>\', \'<1:11>\']\", \"[\'<6:11>\', \'<8:11>\']\"]", str(m1*m2))

    def test_mul_wrong_dimensions(self):
        x = [TwistedInt(1,11), TwistedInt(2,11)]
        y = [TwistedInt(3,11), TwistedInt(4,11)]
        z = [TwistedInt(5,11), TwistedInt(6,11)]
        x1 = [TwistedInt(7,11), TwistedInt(8,11)]
        y1 = [TwistedInt(9,11), TwistedInt(10,11)]
        m1 = TwistedMatrix([x,y,z])
        m2 = TwistedMatrix([x1,y1])
        self.assertRaises(ValueError, TwistedMatrix.__mul__, m2,m1)
