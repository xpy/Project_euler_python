import time
from functools import reduce

import helpers

# inputFile = open('resources/', 'r')

start_time = time.perf_counter()

prime_factors = {}


def get_prime_factors(num, primes=()):
    pf = [1]
    for prime in primes:
        if prime > num:
            break
        if num in set_primes:
            pf.append(num)
            break
        while num % prime == 0:
            if prime not in pf:
                pf.append(prime)
            num /= prime
    return pf


primes = (helpers.shieve_primes_to(100000))
set_primes = set(primes)

flist = {}
flist2 = {}
for i in range(1, 10 ** 5 + 1):
    flist[i] = reduce((lambda x, y: x * y), get_prime_factors(i, primes))
    if i % 1000 == 0:
        print(i)

    flist2[(flist[i], i)] = i

# print(flist)
# print(sorted(flist2))
k = 1
result = None
for i in sorted(flist2):
    # print(i, flist2[i])
    if k == 10000:
        # print("AAAAAA", i[1])
        result = i[1]
    k += 1
print(result)
print(time.perf_counter() - start_time)
# 21417
