from sympy import *
import numpy as np


class Spline:
    """
    This class implements splines
    """

    def __init__(self, spline_base, coord_number, a, b):
        """
        :param spline_base:
        :param coord_number:
        :param a:
        :param b:
        """

        k = 1
        self.kx = []
        self.ky = []
        i = -spline_base + 4
        j = -spline_base + 4
        while i <= coord_number - 1 - spline_base + 4:
            while j <= coord_number - 1 - spline_base + 4:
                self.ky.append(j)
                self.kx.append(i)
                k += 1
                j += 1
            i += 1
            j = -spline_base + 4
        self.spHx = a / (coord_number - spline_base + 1)
        self.spHy = b / (coord_number - spline_base + 1)

    @staticmethod
    def unit_step(x):
        if x == 0:
            return np.sign(x) + 1

        return 0.5 * (np.sign(x) + 1)

    def spline_base(self, x):
        return (11 / 20 - x ** 2 / 2 + x ** 4 / 4 - x ** 5 / 12) * (self.unit_step(x) - self.unit_step(x - 1)) + \
               (17 / 40 + (5 * x) / 8 - (7 * x ** 2) / 4 + (5 * x ** 3) / 4 - (3 * x ** 4) / 8 + x ** 5 / 24) * (
                   self.unit_step(x - 1) - self.unit_step(x - 2)) + \
               (243 / 120 - (81 * x) / 24 + (9 * x ** 2) / 4 - (3 * x ** 3) / 4 + x ** 4 / 8 - x ** 5 / 120) * (
                   self.unit_step(x - 2) - self.unit_step(x - 3))

    def d1Bspline3(self, value):
        return value

    def d2Bspline3(self, value):
        return value

    def spline(self, k, x, y):
        return self.spline_base(abs(x / self.spHx - self.kx[k])) * self.spline_base(abs(y / self.spHy - self.ky[k]))

    def d1x(self, k, x, y):
        return np.sign(x / self.spHx - self.kx[k]) / self.spHx * self.d1Bspline3(
            abs(x / self.spHx - self.kx[k])) * self.spline_base(abs(y / self.spHy - self.ky[k]))

    def d1y(self, k, x, y):
        return np.sign(y / self.spHy - self.ky[k]) / self.spHy * self.spline_base(
            abs(x / self.spHx - self.kx[k])) * self.d1Bspline3(
            abs(y / self.spHy - self.ky[k]))

    def d2x(self, k, x, y):
        return 1 / self.spHx ** 2 * self.d2Bspline3(abs(x / self.spHx - self.kx[k])) * self.spline_base(
            abs(y / self.spHy - self.ky[k]))

    def d2y(self, k, x, y):
        return 1 / self.spHy ** 2 * self.spline_base(abs(x / self.spHx - self.kx[k])) * self.d2Bspline3(
            abs(y / self.spHy - self.ky[k]))
