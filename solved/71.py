import time
import helpers
import math

# inputFile = open('resources/', 'r')

start = time.perf_counter()
target = 1000000
# primes = helpers.primesTo(target)
print(time.perf_counter() - start)

targetNum = 3 / 7
best_diff = 1
best_tuple = []
best_tuple_res = 0
for i in reversed(range(1, target + 1)):
    j = math.ceil(i * targetNum)
    while j/i > best_tuple_res:
        a = targetNum - j/i
        if best_diff > a > 0:
            best_tuple = [j, i]
            best_tuple_res = j/i
            best_diff = a
            break
        j -= 1
    if i % 100000 == 0:
        print(i)


print(best_tuple)

print(time.perf_counter() - start)
