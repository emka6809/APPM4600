import numpy as np
import math
from tabulate import tabulate

def driver():

    x0 = np.array([1,1,1])

    F = lambda x: x[0]**2 + 4*x[1]**2 + 4*x[2]**2 - 16
    Fx = lambda x: 2*x[0]
    Fy = lambda x: 8*x[1]
    Fz = lambda x: 8*x[2]


    points = []

    for i in range(100):
        x1 = np.zeros(3)
        d = F(x0) / (Fx(x0)**2 + Fy(x0)**2 + Fz(x0)**2)

        x1[0] = x0[0] - d*Fx(x0)
        x1[1] = x0[1] - d*Fy(x0)
        x1[2] = x0[2] - d*Fz(x0)

        points.append(x1)

        x0 = x1

    print(tabulate(points, headers = ["x", "y", "z"], tablefmt = 'fancy_grid'))

    x = []
    y = []
    z = []

    for i in points:
        x.append(i[0])
        y.append(i[1])
        z.append(i[2])

    [alpha, constant] = convergence_order(1.09364, x)
    print("The order of convergence of x is:", alpha)

    [alpha, constant] = convergence_order(1.36033, y)
    print("The order of convergence of y is:", alpha)

    [alpha, constant] = convergence_order(1.36033, z)
    print("The order of the convergence of z is:", alpha)


def convergence_order(point, vector):
    N = len(vector)
    num = abs(vector[(N-1)] - point)
    denom = abs(vector[(N-2)] - point)
    if (isinstance(num/denom, float)) and (num/denom < 1):
        alpha = 1
        constant = num/denom
        return [alpha, constant]
    alpha = 2
    while num/(denom**alpha) == float("INF"):
        alpha = alpha + 1
    return [alpha, num/(denom**alpha)]

driver()


