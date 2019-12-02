import time
import helpers
import math

# inputFile = open('resources/', 'r')

start = time.clock()
# (n + 1) * n / 2

num1 = 54
num2 = 54
best = 2000000
target = 2000000
bestDiff = 2000000
prevDiff = 200000

for i in range(0, 1414):
    for j in range(0, 1414):
        res = (i + 1) * i / 2 * (j + 1) * j / 2
        diff = target - res
        if abs(diff) < bestDiff:
            bestDiff = abs(diff)
            best = res
            num1 = i
            num2 = j

print(num1 * num2)

print(time.clock() - start)
