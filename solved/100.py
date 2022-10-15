import time
import helpers
import math
from decimal import *

getcontext().prec = 100

# inputFile = open('resources/', 'r')

start = time.perf_counter()


def find_solutions(num):
    for i in helpers.convergents(num):
        if i[0] ** 2 - num * (i[1] ** 2) == 1:
            return i


def solve_diophantine(x, y, a, b, c, d, e, f):
    D = b ** 2 - 4 * a * c
    k = 4 * a * (a * e * e + c * d * d - b * d * e + D * f)

    p = D * y - 2 * a * e + b * d
    q = 2 * a * x + b * y + d
    return {'D': D, 'p': p, 'q': q, 'k': k}


def f(a):
    # d = math.sqrt(-4 * a * a + -4 * a + 4)
    # d = b ** 2 - 4 * (a ** 2 - a) * 2
    d = 4 - 8 * a * (1 - a)
    #    b**2/4 -2 * a**2 +2*a + 1/4 - 1/4 =1
    #    b**2/4 -( 2*a**2 - 2*a + 1/2) +1/2 = 1
    #    b**2/4 - ( (2*a - 1)/(2**.5))**2 +1/2 = 1
    # print(int(d**.5),int(d**.5)**2,d)
    if int(d ** .5) ** 2 != d:
        return False
    print('?')
    b = (2 - 4 * a)
    sqrt_d = Decimal(d).sqrt()
    # print('b', b)
    # print('din', b ** 2 - 4 * (a ** 2 - a) * 2)
    # print('d', d)
    return (b * -1 - sqrt_d) / 4, (b * -1 + sqrt_d) / 4


print(solve_diophantine(1, 1, 2, 0, -1, 2, 1, 0))

# for i in range(10 ** 1, 10 ** 13):
#     res = f(i)
#     if i % 1000000 == 0:
#         print(i)
#     if res and res[0] % 1 == 0:
#         sadf = ((i - res[0]) / i) * ((i - res[0] - 1) / (i - 1))
#         print(i, res, sadf)
#         print(i - res[0], i - res[1])
#         # break

print(time.perf_counter() - start)

(707106783028 / 1000000002604) * (707106783027 / 1000000002603)
