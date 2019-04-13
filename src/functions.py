from demo.console import Solver


def function_first(i, j, x, y):
    return Solver.fi_d1x(j + 1, x, y) * Solver.fi_d1x(i + 1, x, y) + Solver.fi_d1y(j + 1, x, y) * Solver.fi_d1y(i + 1,
                                                                                                                x, y)


def function_second(i, j, x, y):
    return (Solver.fi_d2x(j + 1, x, y) + Solver.fi_d2y(j + 1, x, y)) * (
        (Solver.fi_d2x(i + 1, x, y) + Solver.fi_d2y(i + 1, x, y)))


def function_third(i, j, x, y):
    return Solver.f1(j + 1, x, y) * Solver.f1(i + 1, x, y)
