import time
import helpers
import math

# inputFile = open('resources/', 'r')

start = time.clock()


def f(a):
    # d = math.sqrt(-4 * a * a + -4 * a + 4)
    b = (2 - 4 * a)
    d = math.sqrt(b ** 2 - 4 * (a ** 2 - a) * 2)
    # print('b', b)
    # print('din', b ** 2 - 4 * (a ** 2 - a) * 2)
    # print('d', d)
    return (b * -1 - d) / 4, (b * -1 + d) / 4


for i in range(10 ** 12, 10 ** 13):
    res = f(i)
    if res[0].is_integer():
        sadf = ((i - res[0]) / i) * ((i - res[0] - 1) / (i - 1))
        print(i, res, sadf)
        print(i - res[0], i - res[1])
        # break

print(time.clock() - start)

(707106783028 / 1000000002604) * (707106783027 / 1000000002603)
