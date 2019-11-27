import time
import helpers
import math
from decimal import *

# inputFile = open('resources/', 'r')

start_time = time.clock()

getcontext().prec = 1000

limit = 1000000000

global_primes = helpers.shieve_primes_to(20000)
set_primes = set(global_primes)

global_things = {}


def another_calc(num):
    power = num - 1
    prime_things = {}
    for i in range(num, 1, -1):
        for pf, pp in global_factors[i].items():
            prime_things[pf] = prime_things.get(pf, 0) + power * pp
        power -= 2

    return prime_things


factor_cache = {}


def get_factors(num, factors=None):
    if num in factor_cache:
        return factor_cache[num]
    new_num = num
    primes = global_primes
    factors = factors if factors is not None else {}
    for p in primes:
        while num % p == 0:
            num //= p
            if p not in factors:
                factors[p] = 0
            factors[p] += 1
        if num == 1:
            break
        if num in set_primes:
            if num not in factors:
                factors[num] = 0
            factors[num] += 1
            break
    factor_cache[new_num] = factors
    return factors


mul_cache = {}


def get_mul(pt, pp):
    if (pt, pp) not in mul_cache:
        mul_cache[(pt, pp)] = (pow(pt, (pp + 1)) - 1) // (pt - 1)
    return mul_cache[(pt, pp)]


# def get_mul2()

global_factors = {}
for i in range(20001, 0, -1):
    global_factors[i] = get_factors(i)

print("\033[0;35m global_factors", global_factors, "\033[0m")

ts = 1
for i in range(2, 20001):
    other_things = another_calc(num=i)
    ds = 1
    # print("\033[0;35m'ena'", 'ena', "\033[0m")
    # print("\033[0;35mlen(other_things)", len(other_things), "\033[0m")
    # for pt, pp in other_things.items():
    #     ds *= get_mul(pt, pp) % 1000000007
    #     ds %= 1000000007
    # print("\033[0;35m'ena'", 'dyo', "\033[0m")

    ts += ds
    if i % 100 == 0:
        print("\033[0;35mi 3", i, "\033[0m")

print("\033[0;35mts -------------- ", ts % 1000000007, "\033[0m")
# print("\033[0;35mglobal_things", global_things, "\033[0m")

the_other_nums = []
n = 5
k = 1
for i in range(n, 1, -1):
    end = i - 1
    start = i - k
    print("\033[0;35mstart", start, "\033[0m")
    print("\033[0;35mend", end, "\033[0m")
    the_other_nums.append((i, k * (start + end) // 2))
    k += 1

mmm = 0
for s in [(5, 4), (4, 5), (3, 3), (2, -2)]:
    for i in range(0, s[1]):
        mmm += s[0] ** i

print("\033[0;35mthe_other_nums", the_other_nums, "\033[0m")
print(time.clock() - start_time)
