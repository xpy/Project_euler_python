import time
import helpers
import math

# inputFile = open('resources/', 'r')

start = time.clock()


def f(d, y):
    return math.sqrt(1 + d * (y ** 2))


def fraction_to(num, to=0, a=None, m=0, d=1):
    a = a if a else int(math.sqrt(num))
    print('num', num)
    print('a', a)
    print('m', m)
    print('d', d)
    print('======')

    next_m = d * a - m
    next_d = int((num - next_m ** 2) / d)
    next_a = int((int(math.sqrt(num)) + next_m) / next_d)
    if to > 0:
        fraction_to(num, to - 1, next_a, next_m, next_d)


fraction_to(7, 10)
# max_res = 0
# for i in [i for i in range(2, 1000) if not (i ** .5).is_integer()]:
#     j = 1
#     print('i', i)
#     while True:
#         res = f(i, j)
#         # print('j', j, res)
#         if res.is_integer():
#             max_res = max(res, max_res)
#             print(res, i, j)
#             break
#         j += 1
# print(max_res)
print(time.clock() - start)
