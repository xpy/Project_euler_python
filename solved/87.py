import time
import helpers
import math
import itertools

# inputFile = open('resources/', 'r')
start = time.perf_counter()
limit = 50000000
primes = (helpers.primes_to(int(limit ** .5)))
limits = {2: limit ** (1 / 2), 3: limit ** (1 / 3), 4: limit ** (1 / 4)}
nums = set()
k = 0
for i in itertools.combinations_with_replacement(primes, 3):
    for j in itertools.permutations([2, 3, 4], 3):
        num = 0
        flag = True
        for f in range(0, 3):
            if i[f] > limits[j[f]]:
                flag = False
                continue
            num += i[f] ** j[f]
            if num > limit:
                flag = False
                continue
        if k % 100000 == 0:
            print(k, num, len(nums), i)
        k += 1
        if not flag:
            continue
        if num < limit:
            nums.add(num)
print(nums)
print(len(nums))

print(time.perf_counter() - start)
