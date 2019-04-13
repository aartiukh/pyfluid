import numpy as np
from algorithms.ready_matrixes import hi_kvadrat,upsilon_kvadrat,gamma_kvadrat, vector_one, vector_two


def hi_kvadrat_inverse():
    inverse_hi_kvadrat = np.linalg.inv(hi_kvadrat.hi_kvadtar())
    return inverse_hi_kvadrat

def mult_upsilon():
    return hi_kvadrat_inverse() @ upsilon_kvadrat.upsilon_kvadrat()

def mult_vector():
    return hi_kvadrat_inverse() @ vector_one.vector_one()

def gamma_kvadrat_inverse():
    return np.linalg.inv(gamma_kvadrat.gamma_kvadrat())

def mult_gamma():
    return gamma_kvadrat_inverse() @ vector_two.vector_two()