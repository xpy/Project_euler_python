import time
import helpers
import math
import itertools

# inputFile = open('resources/', 'r')
start = time.perf_counter()
limit = 50000000
primes = (helpers.primes_to(int(limit ** .5) + 1))

nums = set()
num = [0, 0, 0]
num_of_nums = 0
for i in primes:
    num = [i ** 2, 0, 0]
    for j in primes:
        num[1] = j ** 3
        if sum(num) < limit:
            for k in primes:
                num[2] = k ** 4
                if sum(num) < limit:
                    nums.add(sum(num))
                else:
                    num[2] = 0
                    break
        else:
            break
print(len(nums))
print(time.perf_counter() - start)
