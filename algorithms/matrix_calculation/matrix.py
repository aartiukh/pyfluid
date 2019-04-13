import numpy as np
import time
from algorithms.numerical_integration.integration import Integration
from demo.console import Solver
from algorithms.coord_functions.spline import *
import json, codecs

a = 1
b = 1
nu = 1
T = 5

NN = 225

spline = Spline(6, 15, a, b)
integration = Integration(0.1, 10, 10, 16)

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


def function_first(i, j, x, y):
    return Solver.fi_d1x(j + 1, x, y) * Solver.fi_d1x(i + 1, x, y) + Solver.fi_d1y(j + 1, x, y) * Solver.fi_d1y(i + 1,
                                                                                                                x, y)


def matrix_first():
    res_one = 0
    res_two = 0
    result = np.zeros((NN, NN), dtype=float)
    for i in range(NN):
        print(i)
        for j in range(i, NN):
            if not spline.is_outside(i, j):
                for mx in range(integration.Nx):
                    for my in range(integration.Ny):
                        res_one += ((a1[mx + 1] - a1[mx]) / 2 * (b1[my + 1] - b1[my]) / 2)
                        for ll in range(integration.NN1):
                            for kk in range(integration.NN1):
                                res_two += (aa1[ll] * aa1[kk] *
                                            function_first(i, j, (a1[mx + 1] + a1[mx]) / 2 + (
                                                a1[mx + 1] - a1[mx]) / 2 * sol[kk],
                                                           (b1[my + 1] + b1[my]) / 2 + (
                                                               b1[my + 1] - b1[my]) / 2 * sol[ll]))
                        res_one *= res_two
                        result[i][j] += res_one
                        res_one = 0
                        res_two = 0
                result[j][i] = result[i][j]
    return result


def function_second(i, j, x, y):
    return (Solver.fi_d2x(j + 1, x, y) + Solver.fi_d2y(j + 1, x, y)) * (
    (Solver.fi_d2x(i + 1, x, y) + Solver.fi_d2y(i + 1, x, y)))


def matrix_two():
    res_one = 0
    res_two = 0
    result = np.zeros((NN, NN), dtype=float)
    for i in range(NN):
        print(i)
        for j in range(i, NN):
            if not spline.is_outside(i, j):
                for mx in range(integration.Nx):
                    for my in range(integration.Ny):
                        res_one += ((a1[mx + 1] - a1[mx]) / 2 * (b1[my + 1] - b1[my]) / 2)
                        for ll in range(integration.NN1):
                            for kk in range(integration.NN1):
                                res_two += (aa1[ll] * aa1[kk] *
                                            function_second(i, j, (a1[mx + 1] + a1[mx]) / 2 + (
                                                a1[mx + 1] - a1[mx]) / 2 * sol[kk],
                                                           (b1[my + 1] + b1[my]) / 2 + (
                                                               b1[my + 1] - b1[my]) / 2 * sol[ll]))
                        res_one *= res_two
                        result[i][j] += res_one
                        res_one = 0
                        res_two = 0
                result[j][i] = result[i][j]
    return result


def function_third(i, j, x, y):
    return Solver.f1(j + 1, x, y) * Solver.f1(i + 1, x, y)


def matrix_thirt():
    res_one = 0
    res_two = 0
    result = np.zeros((NN, NN), dtype=float)
    for i in range(NN):
        print(i)
        for j in range(i, NN):
            if not spline.is_outside(i, j):
                for mx in range(integration.Nx):
                    for my in range(integration.Ny):
                        res_one += ((a1[mx + 1] - a1[mx]) / 2 * (b1[my + 1] - b1[my]) / 2)
                        for ll in range(integration.NN1):
                            for kk in range(integration.NN1):
                                res_two += (aa1[ll] * aa1[kk] *
                                            function_third(i, j, (a1[mx + 1] + a1[mx]) / 2 + (
                                                a1[mx + 1] - a1[mx]) / 2 * sol[kk],
                                                           (b1[my + 1] + b1[my]) / 2 + (
                                                               b1[my + 1] - b1[my]) / 2 * sol[ll]))
                        res_one *= res_two
                        result[i][j] += res_one
                        res_one = 0
                        res_two = 0
                result[j][i] = result[i][j]
    return result


if __name__ == '__main__':

    start_time = time.time()
    gamma_kvadrat = matrix_thirt().tolist()
    print("--- %s seconds gamma_kvadrat---" % (time.time() - start_time))
    
    json.dump(gamma_kvadrat, codecs.open("gamma_kvadrat.txt", 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True,
              indent=1)

