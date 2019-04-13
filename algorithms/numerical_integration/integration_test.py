import unittest

from algorithms.numerical_integration.integration import Integration


class TestIntegration(unittest.TestCase):
    def test_a1(self):
        integration = Integration(0.1, 10, 10, 16)
        self.assertEquals(integration.a1()[0], 0)
        self.assertEquals(integration.a1()[2], 0.2)
        self.assertEquals(integration.a1()[10], 1)

    def test_b1(self):
        integration = Integration(0.1, 10, 10, 16)
        self.assertEquals(integration.b1()[0], 0)
        self.assertEquals(integration.b1()[2], 0.2)
        self.assertEquals(integration.b1()[10], 1)

    def test_sol(self):
        integration = Integration(0.1, 10, 10, 16)
        self.assertEquals(integration.sol()[0], -0.9894009349916499325961542)
        self.assertEquals(integration.sol()[2], -0.8656312023878317438804679)
        self.assertEquals(integration.sol()[5], -0.4580167776572273863424194)

    def test_aa1(self):
        integration = Integration(0.1, 10, 10, 16)
        self.assertEquals(round(integration.aa1()[0], 10), 0.0271524594)
        self.assertEquals(round(integration.aa1()[2], 9), 0.095158512)
        self.assertEquals(round(integration.aa1()[5], 10), 0.1691565194)
'''
    def test_int_cpu(self):
        integration = Integration(0.1, 10, 10, 16)
        self.assertAlmostEquals(integration.int_cpu()[0], 2.31012876834319e-11)
        self.assertAlmostEquals(integration.int_cpu()[4], 3.28472830300729e-8)
        self.assertAlmostEquals(integration.int_cpu()[9], 3.46080285359637e-8)
'''
