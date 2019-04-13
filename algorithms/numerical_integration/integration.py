import sympy as sp

from numba import *

from demo.console import Solver


class Integration:
    def __init__(self, step, Nx, Ny, NN1):
        self.step = step
        self.Nx = Nx
        self.Ny = Ny
        self.NN1 = NN1
        self.P = []
        self.row_first = []
        self.row_thirt = []

        x = sp.Symbol('x')
        polynomial = sp.legendre(self.NN1, x)
        solution = sp.solve(polynomial)

        for i in range(len(solution)):
            self.P.append(sp.N(solution[i].n(22)))

    def a1(self):
        a = []
        for i in range(self.Nx + 1):
            a.append(i * self.step)
        return a

    def b1(self):
        b = []
        for i in range(self.Ny + 1):
            b.append(i * self.step)
        return b

    def sol(self):
        return self.P

    def row_first_thirt(self):
        t = sp.Symbol('t')
        k = 0
        arr_f = []
        arr_s = []
        t_row = []
        f_row = []
        for kk in range(0, self.NN1):
            if kk == 0:
                f_row.append(1)
                t_row.append(1)
            else:
                f_row.append((t - self.P[kk - 1]) * f_row[kk - 1])
                for i in range(kk):
                    arr_f.append(self.P[kk] - self.P[i])
                while k < len(arr_f):
                    if k == 0:
                        arr_s.append(arr_f[0])
                    else:
                        arr_s.append((arr_f[k]) * arr_s[k - 1])
                    k += 1
                k = 0
                t_row.append(arr_s[len(arr_s) - 1])
                arr_s = []
                arr_f = []
        return f_row, t_row

    def row_second_fourth(self):
        t = sp.Symbol('t')
        k = 1
        arr_row_second = []
        row_second = []
        arr_row_four = []
        row_four = []
        for kk in range(self.NN1):
            for i in range(kk, self.NN1 - 1):
                if i == kk:
                    arr_row_second.append(t - self.P[i + 1])
                    arr_row_four.append(self.P[kk] - self.P[kk + 1])
                else:
                    arr_row_second.append((t - self.P[i + 1]) * arr_row_second[i - kk - 1])
                    arr_row_four.append((self.P[kk] - self.P[k + kk + 1]) * arr_row_four[k - 1])
                    k += 1
            if (len(arr_row_four) - 1) >= 0:
                row_second.append(arr_row_second[len(arr_row_second) - 1])
                row_four.append(arr_row_four[len(arr_row_four) - 1])
            else:
                row_second.append(1)
                row_four.append(1)
            arr_row_second = []
            arr_row_four = []
            k = 1
        return row_second, row_four

    def aa1(self):
        t = sp.Symbol('t')
        arr = []
        for i in range(self.NN1):
            arr.append(
                sp.integrate(
                    (self.row_first_thirt()[0][i] * self.row_second_fourth()[0][i]) / (
                        self.row_first_thirt()[1][i] * self.row_second_fourth()[1][i]),
                    (t, -1, 1)).n(22))
        return arr

    def fifi1(self, i, x, y):
        return Solver.fi1(i + 1, x, y) ** 2

    def int_cpu(self):
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

        i = 0
        res_one = 0
        res_two = 0
        res = 0
        normfi = []
        mas = []
        while i < 225:
            for mx in range(self.Nx):
                for my in range(self.Ny):
                    res_one += ((a1[mx + 1] - a1[mx]) / 2 * (b1[my + 1] - b1[my]) / 2)
                    for ll in range(self.NN1):
                        for kk in range(self.NN1):
                            res_two += (aa1[ll] * aa1[kk] *
                                        self.fifi1(i, (a1[mx + 1] + a1[mx]) / 2 + (
                                            a1[mx + 1] - a1[mx]) / 2 * sol[kk],
                                                   (b1[my + 1] + b1[my]) / 2 + (
                                                       b1[my + 1] - b1[my]) / 2 * sol[ll]))
                    res_one *= res_two
                    mas.append(res_one)
                    res_one = 0
                    res_two = 0
            for ii in range(len(mas)):
                res += mas[ii]
            normfi.append(res ** (1 / 2))
            res = 0
            mas = []
            i += 1
        return normfi
