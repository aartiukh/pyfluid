import unittest

from algorithms.matrix_calculation import matrix


class TestMatrix(unittest.TestCase):
    def tests_function_third(self):
        self.assertAlmostEqual(matrix.function_third(0, 0, 0.00052, 0.00052), 0.0699496)
        self.assertAlmostEqual(matrix.function_third(224, 224, 0.00052, 0.00052), 0.)

    def tests_function_first(self):
        self.assertAlmostEqual(matrix.function_first(0, 0, 0.00052, 0.00052), 490163.637566680)
        self.assertAlmostEqual(matrix.function_first(1, 1, 0.00052, 0.00052), 58638.0894162368)
'''
    def tests_matrix_first(self):
        self.assertAlmostEqual(matrix.matrix_first()[0][0],9463.168581168924)
        self.assertAlmostEqual(matrix.matrix_first()[1][0], 5561.847188582238)


    def tests_function_second(self):
        self.assertEqual(matrix.function_second(0, 0, 0.00052, 0.00052), 2205165266625.99)

    def tests_matrix_second(self):
        self.assertAlmostEqual(matrix.matrix_two()[0][0],626798119.6370794)
        self.assertAlmostEqual(matrix.matrix_two()[1][1], 179375626.24457824)


    def tests_function_third(self):
        self.assertAlmostEqual(matrix.function_third(0, 0, 0.00052, 0.00052), 0.0699496)
        self.assertAlmostEqual(matrix.function_third(1, 1, 0.00052, 0.00052), 0.00823096)

    def tests_matrix_third(self):
        self.assertAlmostEqual(matrix.matrix_thirt()[0][0], 0.99999999)
        self.assertAlmostEqual(matrix.matrix_thirt()[1][0], 0.8152991144997183)
        self.assertAlmostEqual(matrix.matrix_thirt()[1][1], 1.0000000000450224)
'''
