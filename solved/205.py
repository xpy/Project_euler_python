import time
import helpers
import math
import itertools
from decimal import *

getcontext().prec = 7
# inputFile = open('resources/', 'r')

start_time = time.perf_counter()


def combs(n, r):
    return math.factorial(r + n - 1) / (math.factorial(r) * math.factorial(n - 1))


pyr = {}
pyr_combs = 0
for i in itertools.product([1, 2, 3, 4], repeat=9):
    pyr_combs += 1
    pyr[sum(i)] = pyr.get(sum(i), 0) + 1
sq = {}
sq_combs = 0
for i in itertools.product([1, 2, 3, 4, 5, 6], repeat=6):
    sq_combs += 1
    sq[sum(i)] = sq.get(sum(i), 0) + 1

# pyr_combs = combs(4, 9)
# sq_combs = combs(6, 6)
print(pyr_combs)
print(sq_combs)
results = {}
for i in sorted(pyr):
    other = 0
    for j in sq:
        if i > j:
            other += (sq[j])
    results[i] = ((pyr[i] / pyr_combs) * (other / sq_combs))
summa = 0
for i in results:
    summa += results[i]
print('summa', format(summa, '.7f'))

print(time.perf_counter() - start_time)
