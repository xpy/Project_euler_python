import time
import helpers
import math

# inputFile = open('resources/', 'r')

start = time.clock()
target = 1000000
# primes = helpers.primesTo(target)
print(time.clock() - start)

total = 0
ordered_primes = helpers.shieve_primes_to(target)
primes = set(ordered_primes)

max_loops = 0


def totient(target_number):
    global ordered_primes, max_loops
    new_num = target_number
    for i in ordered_primes:
        if target_number % i == 0:
            new_num *= (i - 1) / i
            while target_number % i == 0:
                target_number /= i
            if target_number in primes:
                new_num *= (target_number - 1) / target_number
                break
        if i > target_number:
            break
    return int(new_num)


for i in range(2, target + 1):
    if i % 10000 == 0:
        print(i, total)
    total += i - 1 if i in primes else totient(i)

print('??', total)

print(time.clock() - start)

# 7295372
