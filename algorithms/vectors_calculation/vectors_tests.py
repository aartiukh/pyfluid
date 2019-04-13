import unittest

from algorithms.vectors_calculation import vecors
import sympy as sp


class Vectors(unittest.TestCase):
    def test_u0(self):
        self.assertAlmostEqual(vecors.u0(0.1, 0.2), 0.)
        self.assertAlmostEqual(vecors.u0(0.2, 0.3), 0.)

    def test_F1(self):
        self.assertAlmostEqual(vecors.F1(0.1, 0.2, 0.3), 0.06186859841958389)
        self.assertAlmostEqual(vecors.F1(0.3, 0.2, 0.1), 0.025804183186522653)

    def test_F2(self):
        self.assertAlmostEqual(vecors.F2(0.1, 0.2, 0.3), -0.17683876203729312)
        self.assertAlmostEqual(vecors.F2(0.3, 0.2, 0.1), -0.24535473930124058)

'''
    def test_vector_one(self):
        t = sp.symbols('t')
        self.assertAlmostEqual(vecors.vector_one()[0],-539.6375615020955 + 539.6337433969725*sp.exp(-t))

    def test_vector_two(self):
        self.assertAlmostEqual(vecors.vector_two()[0],0.)

'''
