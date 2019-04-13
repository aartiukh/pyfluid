import unittest
import sympy as sp
from algorithms.SDE import preparation_SDE


class TestMatrix(unittest.TestCase):
    def tests_hi_kvadrat_inverse(self):
        self.assertAlmostEqual(preparation_SDE.hi_kvadrat_inverse()[0][0], 0.00419156)
        self.assertAlmostEqual(preparation_SDE.hi_kvadrat_inverse()[2][2], 0.0420067)

    def tests_mult_upsilon(self):
        self.assertAlmostEqual(preparation_SDE.mult_upsilon()[0][0], 284295.6105151176)
        self.assertAlmostEqual(preparation_SDE.mult_upsilon()[9][9], 16130.401170289313)

    def tests_gamma_kvadrat_inverse(self):
        self.assertAlmostEqual(preparation_SDE.gamma_kvadrat_inverse()[0][0], 59.6035235155373)
        self.assertAlmostEqual(preparation_SDE.gamma_kvadrat_inverse()[9][9], 43.16746123499798)

    def tests_mult_gamma(self):
        self.assertAlmostEqual(preparation_SDE.mult_gamma()[1], 0.)
        self.assertAlmostEqual(preparation_SDE.mult_gamma()[5], 0.)
'''
    def tests_mult_vector(self):
        t = sp.symbols('t')
        self.assertAlmostEqual(preparation_SDE.mult_vector()[0][0], 0)
        self.assertAlmostEqual(preparation_SDE.mult_vector()[0][0], 0)
'''
