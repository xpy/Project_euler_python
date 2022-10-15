import time
import helpers
import math

# inputFile = open('resources/', 'r')

start_time = time.perf_counter()

cache = {}
k = 1
mc = 0
bn = 0
while k < 10 ** 6:
    c = 1
    n = k
    while n > 1:
        if n in cache:
            c += cache[n]
            break
        n = 3 * n + 1 if n % 2 else n / 2
        c += 1
    cache[k] = c
    if c > mc:
        mc = c
        bn = k
    k += 1
print("\033[0;35mmc", mc, bn, "\033[0m")

print(time.perf_counter() - start_time)
