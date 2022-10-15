import time
import helpers
import math

# inputFile = open('resources/', 'r')

start = time.perf_counter()

# print(fraction(23))
num = 1
existing = {}
target = 1500000
# for num in range(1, top):
while num ** 2 < target:
    num2 = num + 1
    asdf = 0
    increment = 2 if num % 2 else 1
    while asdf < target:
        if helpers.are_relative_prime(num, num2):
            asdf = 2 * (num2 * (num + num2))
            k = 1
            asdf2 = k * asdf
            while asdf2 < target:
                existing[asdf2] = existing.get(asdf2, set())
                existing[asdf2].add((num * k, num2 * k))
                k += 1
                asdf2 += asdf
        num2 += increment
    num += 1

counter = 0
for i in existing:
    if len(existing[i]) == 1:
        counter += 1
        # print(i, existing[i])
print(counter)
print(time.perf_counter() - start)

# 355570
# 161667
