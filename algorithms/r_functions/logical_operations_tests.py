# __author__ = 'artyukhanton@gmail.com'

import unittest
from sympy import *

from algorithms.r_functions import logical_operations


class TestLogicalOperations(unittest.TestCase):
    def test_conjunction(self):
        self.assertEqual(logical_operations.conjunction(0, 1, 1), 2 - sqrt(2))
        self.assertEqual(logical_operations.conjunction(0, 2, 1), 3 - sqrt(5))

    def test_disjunction(self):
        self.assertEqual(logical_operations.disjunction(0, 1, 1), 2 + sqrt(2))
        self.assertEqual(logical_operations.disjunction(0, 2, 1), 3 + sqrt(5))

    def test_property_second(self):
        self.assertEquals(logical_operations.conjunction(0, 2, 1), logical_operations.conjunction(0, 1, 2))
        self.assertEquals(logical_operations.conjunction(0, 4, 5), logical_operations.conjunction(0, 5, 4))

    def test_property_third(self):
        self.assertEquals(logical_operations.disjunction(0, 2, 1), logical_operations.disjunction(0, 1, 2))
        self.assertEquals(logical_operations.disjunction(0, 4, 5), logical_operations.disjunction(0, 5, 4))

    def test_property_fourth(self):
        self.assertEquals(-logical_operations.conjunction(0, 1, 1), logical_operations.disjunction(0, -1, -1))
        self.assertEquals(-logical_operations.conjunction(0, 2, 1), logical_operations.disjunction(0, -2, -1))

    def test_property_fifth(self):
        self.assertEquals(-logical_operations.disjunction(0, 1, 1), logical_operations.conjunction(0, -1, -1))
        self.assertEquals(-logical_operations.disjunction(0, 2, 1), logical_operations.conjunction(0, -2, -1))

    def test_property_sixth(self):
        self.assertEquals(logical_operations.disjunction(0, 1, 1) + logical_operations.conjunction(0, 1, 1), 4)
        self.assertEquals(logical_operations.disjunction(0, 2, 1) + logical_operations.conjunction(0, 2, 1), 6)

    def test_property_seventh(self):
        self.assertAlmostEqual(logical_operations.disjunction(0, 1, 1) * logical_operations.conjunction(0, 1, 1), 2)
        self.assertAlmostEqual(logical_operations.disjunction(0, 2, 1) * logical_operations.conjunction(0, 2, 1), 4)

    def test_property_eighth(self):
        self.assertEquals(logical_operations.conjunction(0, 0, 5), 0)
        self.assertEquals(logical_operations.conjunction(0, 5, 0), 0)

    def test_property_ninth(self):
        self.assertEquals(logical_operations.disjunction(0, 0, -5), 0)
        self.assertEquals(logical_operations.disjunction(0, -5, 0), 0)

    def test_property_tenth(self):
        self.assertEquals(logical_operations.conjunction(1, 1, 1), 1)
        self.assertEquals(logical_operations.conjunction(1, 2, 2), 2)

    def test_property_eleventh(self):
        self.assertEquals(logical_operations.disjunction(1, 1, 1), 1)
        self.assertEquals(logical_operations.disjunction(1, 2, 2), 2)

    def test_property_twelfth(self):
        self.assertEquals(logical_operations.conjunction(1, 1, -1), -abs(1))
        self.assertEquals(logical_operations.conjunction(1, -1, 1), -abs(-1))

    def test_property_thirteenth(self):
        self.assertEquals(logical_operations.disjunction(1, 1, -1), abs(1))
        self.assertEquals(logical_operations.disjunction(1, -1, 1), abs(-1))

    def test_property_fourteenth(self):
        self.assertEquals(logical_operations.conjunction(1, 1, logical_operations.conjunction(1, 1, 1)),
                          logical_operations.conjunction(1, logical_operations.conjunction(1, 1, 1), 1))
        self.assertEquals(logical_operations.conjunction(1, 1, logical_operations.conjunction(1, 2, 3)),
                          logical_operations.conjunction(1, logical_operations.conjunction(1, 1, 2), 3))

    def test_property_fifteenth(self):
        self.assertEquals(logical_operations.disjunction(1, 1, logical_operations.disjunction(1, 1, 1)),
                          logical_operations.disjunction(1, logical_operations.disjunction(1, 1, 1), 1))
        self.assertEquals(logical_operations.disjunction(1, 1, logical_operations.disjunction(1, 2, 3)),
                          logical_operations.disjunction(1, logical_operations.disjunction(1, 1, 2), 3))

    def test_property_sixteenth(self):
        self.assertEquals(logical_operations.conjunction(1, 1, logical_operations.disjunction(1, 1, 1)),
                          logical_operations.disjunction(1, logical_operations.conjunction(1, 1, 1),
                                                         logical_operations.conjunction(1, 1, 1)))
        self.assertEquals(logical_operations.conjunction(1, 1, logical_operations.disjunction(1, 2, 3)),
                          logical_operations.disjunction(1, logical_operations.conjunction(1, 1, 2),
                                                         logical_operations.conjunction(1, 1, 3)))

    def test_property_seventeenth(self):
        self.assertEquals(logical_operations.disjunction(1, 1, logical_operations.conjunction(1, 1, 1)),
                          logical_operations.conjunction(1, logical_operations.disjunction(1, 1, 1),
                                                         logical_operations.disjunction(1, 1, 1)))
        self.assertEquals(logical_operations.disjunction(1, 1, logical_operations.conjunction(1, 2, 3)),
                          logical_operations.conjunction(1, logical_operations.disjunction(1, 1, 2),
                                                         logical_operations.disjunction(1, 1, 3)))

    def test_property_eighteenth(self):
        self.assertEquals(logical_operations.disjunction(1, logical_operations.conjunction(1, 1, 1), 1), 1)
        self.assertEquals(logical_operations.disjunction(1, logical_operations.conjunction(1, 1, 2), 1), 1)

    def test_property_nineteenth(self):
        self.assertEquals(logical_operations.conjunction(1, logical_operations.disjunction(1, 1, 1), 1), 1)
        self.assertEquals(logical_operations.conjunction(1, logical_operations.disjunction(1, 1, 2), 1), 1)


if __name__ == '__main__':
    unittest.main()
