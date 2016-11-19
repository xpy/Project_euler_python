import time
import helpers
import math
import itertools

# inputFile = open('resources/', 'r')

start = time.clock()

target = 10000000
ordered_primes = helpers.shieve_primes_to(target)
primes = set(ordered_primes)


def totient(target_number):
    global ordered_primes, minimum
    new_num = target_number
    for i in ordered_primes:
        if target_number % i == 0:
            new_num *= (i - 1) / i
            while target_number % i == 0:
                target_number /= i
            if target_number in primes:
                new_num *= (target_number - 1) / target_number
                break
            if target_number / new_num > minimum:
                return 1
        if i > target_number:
            break
    return int(new_num)


# number = 87109

minimum = 2
for i in range(1, target):
    if i in primes:
        continue
    if i % 100000 == 0:
        print(i, minimum)
    num = totient(i)
    if helpers.is_permutation(num, i) and num != i:
        res = [i, num, i / num]
        if i / num < minimum:
            minimum = i / num
            print(res)

# totients = totient(number)
# print(totients)

print(time.clock() - start)
