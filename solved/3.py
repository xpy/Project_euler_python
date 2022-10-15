import time

import helpers


# inputFile = open('resources/', 'r')


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


start_time = time.perf_counter()
prime_factors = {}
num = 600851475143
primes = (helpers.shieve_primes_to(int(num**.5)))
print('found primes')
set_primes = set(primes)

pf = get_prime_factors(num, primes)
print("\033[0;35mpf", pf, "\033[0m")

print(time.perf_counter() - start_time)
