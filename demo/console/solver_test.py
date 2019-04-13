import unittest

from demo.console import Solver


class TestSolver(unittest.TestCase):
    def tests_f1(self):
        self.assertAlmostEqual(Solver.f1(1, 0.00052, 0.00052), 15.2862925710854)

    def test_fi_d1x(self):
        self.assertAlmostEqual(Solver.fi_d1x(100, 0.5, 0.63), -44.0113156218353)
        self.assertAlmostEqual(Solver.fi_d1x(225, 0.5, 0.63), 0.)

    def test_fi_d1y(self):
        self.assertAlmostEqual(Solver.fi_d1y(100, 0.5, 0.63), 27.1194750486313)
        self.assertAlmostEqual(Solver.fi_d1y(225, 0.5, 0.63), 0.)

    def test_fi_d2x(self):
        self.assertAlmostEqual(Solver.fi_d2x(100, 0.5, 0.63), 334.687043158630)
        self.assertAlmostEqual(Solver.fi_d2x(225, 0.5, 0.63), 0.)

    def test_fi_d2y(self):
        self.assertAlmostEqual(Solver.fi_d2y(100, 0.5, 0.63), -158.512374183982)
        self.assertAlmostEqual(Solver.fi_d2y(225, 0.5, 0.63), 0.)

    def test_fifi(self):
        self.assertAlmostEqual(Solver.fifi(0.1, 0.2, 0.3), 0.00139761)
        self.assertAlmostEqual(Solver.fifi(0.5, 0.2, 0.3), 0.00409637)


if __name__ == '__main__':
    unittest.main()
