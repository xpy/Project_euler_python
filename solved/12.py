import time
import helpers
import math

# inputFile = open('resources/', 'r')
start = time.perf_counter()

primes = helpers.shieve_primes_to(100000)
primes_set = set(primes)
divisor_cache = {}
i = 1
num = 0
max_prime = 0
while True:
    num = num + i
    i += 1
    divisors = {}
    tmp_num = num
    if num % 2:
        continue
    for prime in primes:
        power = 0
        while tmp_num % prime == 0:
            tmp_num /= prime
            power += 1
        if power > 0:
            divisors[prime] = power
        if tmp_num == 1:
            break
        if tmp_num in primes_set:
            divisors[tmp_num] = 1
            break

    result = 1
    for divisor in divisors:
        result *= divisors[divisor] + 1
    if result > 500:
        print(num)
        break

print(time.perf_counter() - start)
