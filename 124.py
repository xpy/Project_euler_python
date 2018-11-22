import time
import helpers
import math
from functools import reduce

# inputFile = open('resources/', 'r')

start_time = time.clock()


def get_prime_factors(num, primes=[]):
    if num in primes:
        return [num]
    pf = [1]
    for prime in primes:
        if prime > num:
            break
        if num % prime == 0:
            pf.append(prime)
            num /= prime
    return pf


primes = helpers.shieve_primes_to(100000)

flist = {}
flist2 = {}
for i in range(1, 10 ** 5 + 1):
    flist[i] = reduce((lambda x, y: x * y), get_prime_factors(i, primes))
    if i % 1000 == 0:
        print(i)

    flist2[(flist[i], i)] = i

print(flist)
print(sorted(flist2))
k = 1
result = None
for i in sorted(flist2):
    print(i, flist2[i])
    if k == 10000:
        print("AAAAAA", i[1])
        result = i[1]
    k += 1
print(result)
print(time.clock() - start_time)
# 21417
