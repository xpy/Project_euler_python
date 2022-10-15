import time
import helpers
import math

# inputFile = open('resources/', 'r')

start = time.perf_counter()

cache = {}
cache2 = {}


def factorial(num):
    c = cache.get(num)
    if c:
        return c
    cache[num] = 1 if num == 0 else num * factorial(num - 1)
    return cache[num]


def do_the_thing(num):
    c = cache2.get(num)
    if c:
        return c
    s = 0
    for digit in str(num):
        s += factorial(int(digit))
    cache2[num] = s
    return s

k = 0
for i in range(1, 1000000):
    if i % 10000 == 0:
        print(i)
    buffer = {i}
    res = do_the_thing(i)
    while res not in buffer:
        buffer |= {res}
        res = do_the_thing(res)
    if len(buffer) == 60:
        # print(buffer)
        k += 1
print(k)
print(time.perf_counter() - start)
