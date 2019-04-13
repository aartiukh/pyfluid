from demo.console import Solver
from algorithms.r_functions.logical_operations import *
from algorithms.numerical_integration.integration import Integration

import sympy as sp

integration = Integration(0.1, 10, 10, 16)

x, y, t = sp.symbols('x y t')

sol = [-0.989400934991650,
       -0.944575023073233,
       -0.865631202387832,
       -0.755404408355003,
       -0.617876244402644,
       -0.458016777657227,
       -0.281603550779259,
       -0.0950125098376374,
       0.0950125098376374,
       0.281603550779259,
       0.458016777657227,
       0.617876244402644,
       0.755404408355003,
       0.865631202387832,
       0.944575023073233,
       0.989400934991650]
a1 = [0., 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.]
b1 = [0., 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.]
aa1 = [0.02715245941202937274284, 0.06225352394034011638269,
       0.09515851168322342346073, 0.1246289712652290937456,
       0.1495959888184188457672, 0.1691565194053055165568,
       0.1826034150233368791305, 0.1894506104454194428399,
       0.1894506104640640842263, 0.1826034150411857126528,
       0.1691565194036002139910, 0.1495959888154629879864,
       0.1246289712534291993506, 0.09515851168185918140807,
       0.06225352393869343359256, 0.02715245941181976263579]


def fi0(x, y):
    return 0


def u0(x, y):
    return fi0(x, y) - Solver.fifi(x, y, 0)


def fifi(x, y, t):
    return Solver.f(x, y, t) - Solver.omega(x, y) * (Solver.omega_d1x_sym(x, y) * Solver.f_d1x_sym(x, y, t) +
                                                     Solver.omega_d1y_sym(x, y) * Solver.f_d1y_sym(x, y, t) + Solver.g(
        x, y, t))


def fifi_d2x_sym(x, y, t):
    return sp.diff(fifi(x, y, t), x, 2)


def fifi_d2y_sym(x, y, t):
    return sp.diff(fifi(x, y, t), y, 2)


def F1_sym(x, y, t):
    return -1 * (fifi_d2x_sym(x, y, t) + fifi_d2y_sym(x, y, t))


F1 = sp.lambdify((x, y, t), F1_sym(x, y, t), "numpy")


def F2_sym(x, y, t):
    return sp.diff((fifi_d2x_sym(x, y, t) + fifi_d2y_sym(x, y, t)), t)


F2 = sp.lambdify((x, y, t), F2_sym(x, y, t), "numpy")


def function_one(i, x, y):
    return F1(x, y, t) * (Solver.fi_d2x(i, x, y) + Solver.fi_d2y(i, x, y)) + F2(x, y, t) * Solver.f1(i, x, y)


def vector_one():
    i = 0
    res_one = 0
    res_two = 0
    res = 0
    result = []
    mas = []
    while i < 1:
        for mx in range(integration.Nx):
            for my in range(integration.Ny):
                res_one += ((a1[mx + 1] - a1[mx]) / 2 * (b1[my + 1] - b1[my]) / 2)
                for ll in range(integration.NN1):
                    for kk in range(integration.NN1):
                        res_two += (aa1[ll] * aa1[kk] *
                                    function_one(i, (a1[mx + 1] + a1[mx]) / 2 + (
                                        a1[mx + 1] - a1[mx]) / 2 * sol[kk],
                                                 (b1[my + 1] + b1[my]) / 2 + (
                                                     b1[my + 1] - b1[my]) / 2 * sol[ll]))
                res_one *= res_two
                mas.append(res_one)
                res_one = 0
                res_two = 0
        for ii in range(len(mas)):
            res += mas[ii]
        result.append(res)
        res = 0
        mas = []
        i += 1
    return result


def function_two(i, x, y):
    return u0(x, y) * Solver.f1(i + 1, x, y)


def vector_two():
    i = 0
    res_one = 0
    res_two = 0
    res = 0
    result = []
    mas = []
    while i < 225:
        for mx in range(integration.Nx):
            for my in range(integration.Ny):
                res_one += ((a1[mx + 1] - a1[mx]) / 2 * (b1[my + 1] - b1[my]) / 2)
                for ll in range(integration.NN1):
                    for kk in range(integration.NN1):
                        res_two += (aa1[ll] * aa1[kk] *
                                    function_two(i, (a1[mx + 1] + a1[mx]) / 2 + (
                                        a1[mx + 1] - a1[mx]) / 2 * sol[kk],
                                                 (b1[my + 1] + b1[my]) / 2 + (
                                                     b1[my + 1] - b1[my]) / 2 * sol[ll]))
                res_one *= res_two
                mas.append(res_one)
                res_one = 0
                res_two = 0
        for ii in range(len(mas)):
            res += mas[ii]
        result.append(res)
        res = 0
        mas = []
        i += 1
    return result
