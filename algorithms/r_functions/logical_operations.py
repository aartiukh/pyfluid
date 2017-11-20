# __author__ = 'artyukhanton@gmail.com'

import math


def conjunction(alpha, x, y):
    """
    Performs R-conjunction
    :param alpha: alpha parameter
    :param x: x-coordinate
    :param y: y -coordinate
    :return: R-conjunction real value
    """
    assert -1 < alpha <= 1

    return (x + y - math.sqrt(x * x + y * y - 2 * alpha * x * y)) / (1 + alpha)


def disjunction(alpha, x, y):
    """
    Performs R-disjunction
    :param alpha: alpha parameter
    :param x: x-coordinate
    :param y: y -coordinate
    :return: R-conjunction real value
    """
    assert -1 < alpha <= 1

    return (x + y + math.sqrt(x * x + y * y - 2 * alpha * x * y)) / (1 + alpha)