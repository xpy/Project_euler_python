import time
import helpers

start_time = time.perf_counter()

global_primes = helpers.shieve_primes_to(20000)
set_primes = set(global_primes)

global_things = {}


def calc_prime_factors(num):
    power = num - 1
    prime_things = {}
    for i in range(num, 1, -1):
        for pf, pp in global_factors[i].items():
            prime_things[pf] = prime_things.get(pf, 0) + power * pp
        power -= 2

    return prime_things


factor_cache = {}
mul_cache = {}


def get_prime_factors(num, factors=None):
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


MOD = 1000000007


def get_mul(pt, pp):
    return (pow(pt, (pp + 1), MOD) - 1) * pow(pt - 1, MOD - 2, MOD)


global_factors = {}
for i in range(20001, 0, -1):
    global_factors[i] = get_prime_factors(i)

ts = 1
for i in range(2, 20001):
    ds = 1
    for pt, pp in calc_prime_factors(i).items():
        ds *= get_mul(pt, pp) % MOD
        ds %= MOD

    ts += ds
    if i % 100 == 0:
        print("\033[0;35mi ", i, "\033[0m")

print("\033[0;35mts -------------- ", ts % MOD, "\033[0m")

print(time.perf_counter() - start_time)
