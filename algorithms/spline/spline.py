from sympy import *
import numpy as np

a = 0.5
b = 0.5
nn = 15
NN = nn**2
splinebase = 6
k = 1
kx = {}
ky = {}
i = -splinebase + 4
j = -splinebase + 4
while(i <= nn - 1 - splinebase + 4):
    while(j <= nn - 1 - splinebase + 4):
        ky[k] = j
        kx[k] = i
        k += 1
        j += 1
    i += 1
    j = -splinebase + 4
spHx = a / (nn - splinebase + 1)
spHy = a / (nn - splinebase + 1)

def unitStep(x):
    if(x == 0):
        return np.sign(x)+1
    else: return 0.5*(np.sign(x)+1)

def f_one(x):
    return (11/20-x**2/2+x**4/4-x**5/12)

def f_two(x):
    return (17/40+(5*x)/8-(7*x**2)/4+(5*x**3)/4-(3*x**4)/8+x**5/24)

def f_three(x):
    return (243/120-(81*x)/24+(9*x**2)/4-(3*x**3)/4+x**4/8-x**5/120)

def dif(value,power):
    x = symbols('x')
    return diff(f_one(x), x, power).subs({x: value}) * (unitStep(value) - unitStep(value - 1)) + \
           diff(f_two(x), x, power).subs({x: value}) * (unitStep(value - 1) - unitStep(value - 2)) + \
           diff(f_three(x), x, power).subs({x: value}) * (unitStep(value - 2) - unitStep(value - 3))

def bspline3(x):
    return f_one(x) * (unitStep(x) - unitStep(x - 1)) + \
           f_two(x) * (unitStep(x - 1) - unitStep(x - 2)) + \
           f_three(x) * (unitStep(x - 2) - unitStep(x - 3))

def d1Bspline3(value):
    return dif(value, 1)

def d2Bspline3(value):
    return dif(value, 2)


def spline(k, x, y):
    return bspline3(abs(x / spHx - kx[k])) * bspline3(abs(y / spHy - ky[k]))

def d1xSpline(k, x, y):
    return np.sign(x / spHx - kx[k])/spHx * d1Bspline3(abs(x /spHx - kx[k])) * bspline3(abs(y/spHy - ky[k]))

def d1ySpline(k, x, y):
    return np.sign(y/spHy - ky[k])/spHy * bspline3(abs(x/spHx - kx[k])) * d1Bspline3(abs(y/spHy - ky[k]))

def d2xSpline(k, x, y):
    return 1/spHx**2 * d2Bspline3(abs(x/spHx - kx[k])) * bspline3(abs(y/spHy - ky[k]))

def d2ySpline(k, x, y):
    return 1/spHy**2 * bspline3(abs(x/spHx - kx[k])) * d2Bspline3(abs(y/spHy - ky[k]))

def coordFunc(k, x, y):
    return spline(k, x, y)

def coordFuncD1x(k, x, y):
    return d1xSpline(k, x, y)

def coordFuncD1y(k, x, y):
    return d1ySpline(k, x, y)

def coordFuncD2x(k, x, y):
    return d2xSpline(k, x, y)

def coordFuncD2y(k, x, y):
    return d2ySpline(k, x, y)