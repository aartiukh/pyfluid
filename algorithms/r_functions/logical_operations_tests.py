# __author__ = 'artyukhanton@gmail.com'

import unittest
import math

from algorithms.r_functions import logical_operations


class TestLogicalOperations(unittest.TestCase):

    def test_conjunction(self):
        self.assertEqual(logical_operations.conjunction(0, 1, 1), 2 - math.sqrt(2))
        self.assertEqual(logical_operations.conjunction(0, 2, 1), 3 - math.sqrt(5))

    def test_disjunction(self):
        self.assertEqual(logical_operations.disjunction(0, 1, 1), 2 + math.sqrt(2))
        self.assertEqual(logical_operations.disjunction(0, 2, 1), 3 + math.sqrt(5))


if __name__ == '__main__':
    unittest.main()
