import time
import helpers
import math
from decimal import *

# inputFile = open('resources/', 'r')

start_time = time.clock()

getcontext().prec = 1000

limit = 1000000000

global_primes = helpers.shieve_primes_to(1000000)
set_primes = set(global_primes)

factorial_cache = {}
tuple_factorial_cache = {}


def another_calc(num):
    power = num // 2 + 1
    nominator = 1
    for i in range(num, 1, -1):
        power -= 1
        nominator *= (i ** power) * 2
        if power == 0 and num % 2 == 0:
            power = -1
    return int(nominator)


5145


def get_fact(num):
    if num not in factorial_cache:
        factorial_cache[num] = math.factorial(num)
    return factorial_cache[num]


def get_fact_tuple(num1, num2):
    key = tuple((sorted((num1, num2))))
    if key not in tuple_factorial_cache:
        tuple_factorial_cache[key] = (get_fact(num1)) * (get_fact(num2))

    return tuple_factorial_cache[key]


fact_mul_cache = {}


def fact_mul(fact, power):
    if (fact, power) not in fact_mul_cache:
        fact_mul_cache[(fact, power)] = (fact ** (power + 1) - 1) // (fact - 1)
    return fact_mul_cache[(fact, power)]


def b2(num):
    fac_num = math.factorial(num)
    factors = {}
    fact_2 = another_calc(num)
    fact3 = 1
    for i in range(1, (num // 2) + num % 2):
        fact = int(fac_num // get_fact_tuple(i, num - i))
        fact3 *= fact * 2
        for key, val in get_factors(fact).items():
            factors[key] = factors.get(key, 0) + (val * 2)
    if num % 2 == 0:
        i = num // 2
        fact = int(fac_num // get_fact_tuple(i, num - i))
        fact3 *= fact
        for key, val in get_factors(fact).items():
            factors[key] = factors.get(key, 0) + val

    for key, val in get_factors(fact3).items():
        factors[key] = factors.get(key, 0) + val
    print("\033[0;35mfact_2", fact_2, "\033[0m")
    print("\033[0;35mfact3", fact3, "\033[0m")
    s = 1
    for fact, power in factors.items():
        s *= fact_mul(fact, power)
        s %= 1000000007
    return s


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


s = Decimal(1)
s2 = 1
for i in range(2, 11):
    # bi = b(i)
    b2i = b2(i)
    # divisors_sum = get_divisors_sum(bi)
    # s += int(divisors_sum)
    s2 += b2i
    print(f"\033[0;35ms{i} - 2 %1000000007", int(s2) % 1000000007, "\033[0m")
332792866
213186352
print(time.clock() - start_time)
