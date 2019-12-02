import time
import helpers
import math

# inputFile = open('resources/', 'r')

start = time.clock()
target = 12000
# primes = helpers.primesTo(target)
print(time.clock() - start)

target_start_num = 1 / 3
target_end_num = 1 / 2
between = 0

for i in range(2, target + 1):
    between += len(
        [j for j in range(math.floor(i * target_start_num), math.ceil(i * target_end_num)) if math.gcd(i, j) == 1])

print(between)

print(time.clock() - start)

# 7295372
