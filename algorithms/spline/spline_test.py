import unittest


from algorithms.spline import spline


class TestSpline(unittest.TestCase):

    def test_unit_step(self):
        self.assertEqual(spline.unitStep(-5), 0)
        self.assertEqual(spline.unitStep(0), 1)
        self.assertEqual(spline.unitStep(5), 1)

    def test_bspline3(self):
        self.assertEquals(round(spline.bspline3(0), 10),round(11/20, 10))
        self.assertEquals(round(spline.bspline3(1), 10),round(13/60, 10))
        self.assertEquals(spline.bspline3(3), 0)


    def test_d1Bspline3(self):
        self.assertEquals(spline.d1Bspline3(0), 0)
        self.assertEquals(round(spline.d1Bspline3(1), 10),round(-5/12, 10))
        self.assertEquals(spline.d1Bspline3(3), 0)


    def test_d2Bspline3(self):
        self.assertEquals(spline.d2Bspline3(0), -1)
        self.assertEquals(round(spline.d2Bspline3(1), 10), round(1/3, 10))
        self.assertEquals(spline.d2Bspline3(3), 0)

    def test_spline(self):
        self.assertEquals(spline.spline(1 ,1 ,1), 0)
        self.assertEquals(spline.spline(2, 2, 2), 0)
        self.assertEquals(spline.spline(3, 3, 3), 0)

    def test_d1xSpline(self):
        self.assertEquals(spline.d1xSpline(1, 1, 1), 0)
        self.assertEquals(spline.d1xSpline(2, 2, 2), 0)
        self.assertEquals(spline.d1xSpline(3, 3, 3), 0)

    def test_d1ySpline(self):
        self.assertEquals(spline.d1ySpline(1, 1, 1), 0)
        self.assertEquals(spline.d1ySpline(2, 2, 2), 0)
        self.assertEquals(spline.d1ySpline(3, 3, 3), 0)

    def test_d2xSpline(self):
        self.assertEquals(spline.d2xSpline(1, 1, 1), 0)
        self.assertEquals(spline.d2xSpline(2, 2, 2), 0)
        self.assertEquals(spline.d2xSpline(3, 3, 3), 0)

    def test_d2ySpline(self):
        self.assertEquals(spline.d1ySpline(1, 1, 1), 0)
        self.assertEquals(spline.d1ySpline(2, 2, 2), 0)
        self.assertEquals(spline.d1ySpline(3, 3, 3), 0)

if __name__ == '__main__':
    unittest.main()