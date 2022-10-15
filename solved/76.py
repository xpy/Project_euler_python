import time
import helpers
import math

# inputFile = open('resources/', 'r')

start = time.perf_counter()

cache = {}


def do_it(num, limit):
    cache_key = (num, limit)
    c = cache.get(cache_key)
    if c:
        return c
    s = 0
    for i in range(limit, 0, -1):
        n2 = num - i
        s += 1 if n2 <= 1 else do_it(n2, min(i, n2))
    cache[cache_key] = s
    return s


print(do_it(100, 99))
# print(cache)
# 190569291

print(time.perf_counter() - start)
