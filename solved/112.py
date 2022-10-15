import time
import helpers
import math

# inputFile = open('resources/', 'r')

start = time.perf_counter()

bouncy_sum = 0
i = 1

# print(helpers.is_bouncy2(543))


while bouncy_sum / i != .99:
    i += 1
    bouncy_sum += 1 if helpers.is_bouncy(i) else 0
    # print(i, helpers.is_bouncy(i), bouncy_sum / i)

print(i)

print(time.perf_counter() - start)
