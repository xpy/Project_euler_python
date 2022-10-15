import time
from decimal import Decimal

import helpers
import math

# inputFile = open('resources/', 'r')

start_time = time.perf_counter()

things = [10 for i in range(0, 7)]


def n_out_of_n(s, ss):
    return math.factorial(s) / (math.factorial(ss) * math.factorial(s - ss))


all_combs = (n_out_of_n(70, 20))
res = (all_combs - (n_out_of_n(60, 20))) / all_combs

print("\033[0;35mres", res * 7, "\033[0m")

print(time.perf_counter() - start_time)
