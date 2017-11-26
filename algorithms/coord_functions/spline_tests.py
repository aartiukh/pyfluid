import unittest

from algorithms.coord_functions.spline import Spline


class TestSpline(unittest.TestCase):
    def test_unit_step(self):
        self.assertEqual(Spline.unit_step(-5), 0)
        self.assertEqual(Spline.unit_step(0), 1)
        self.assertEqual(Spline.unit_step(5), 1)

    def test_bspline3(self):
        spline = Spline(6, 15, 0.5, 0.5)
        self.assertEquals(round(spline.spline_base(0), 10), round(11 / 20, 10))
        self.assertEquals(round(spline.spline_base(1), 10), round(13 / 60, 10))
        self.assertEquals(spline.spline_base(3), 0)

    def test_d1Bspline3(self):
        spline = Spline(6, 15, 0.5, 0.5)
        self.assertEquals(spline.d1Bspline3(0), 0)
        self.assertEquals(round(spline.d1Bspline3(1), 10), round(-5 / 12, 10))
        self.assertEquals(spline.d1Bspline3(3), 0)

    def test_d2Bspline3(self):
        spline = Spline(6, 15, 0.5, 0.5)
        self.assertEquals(spline.d2Bspline3(0), -1)
        self.assertEquals(round(spline.d2Bspline3(1), 10), round(1 / 3, 10))
        self.assertEquals(spline.d2Bspline3(3), 0)

    def test_spline(self):
        spline = Spline(6, 15, 0.5, 0.5)
        self.assertEquals(spline.spline(1, 1, 1), 0)
        self.assertEquals(spline.spline(2, 2, 2), 0)
        self.assertEquals(spline.spline(3, 3, 3), 0)

    def test_d1xSpline(self):
        spline = Spline(6, 15, 0.5, 0.5)
        self.assertEquals(spline.d1x(1, 1, 1), 0)
        self.assertEquals(spline.d1x(2, 2, 2), 0)
        self.assertEquals(spline.d1x(3, 3, 3), 0)

    def test_d1ySpline(self):
        spline = Spline(6, 15, 0.5, 0.5)
        self.assertEquals(spline.d1y(1, 1, 1), 0)
        self.assertEquals(spline.d1y(2, 2, 2), 0)
        self.assertEquals(spline.d1y(3, 3, 3), 0)

    def test_d2xSpline(self):
        spline = Spline(6, 15, 0.5, 0.5)
        self.assertEquals(spline.d2x(1, 1, 1), 0)
        self.assertEquals(spline.d2x(2, 2, 2), 0)
        self.assertEquals(spline.d2x(3, 3, 3), 0)

    def test_d2ySpline(self):
        spline = Spline(6, 15, 0.5, 0.5)
        self.assertEquals(spline.d1y(1, 1, 1), 0)
        self.assertEquals(spline.d1y(2, 2, 2), 0)
        self.assertEquals(spline.d1y(3, 3, 3), 0)


if __name__ == '__main__':
    unittest.main()
