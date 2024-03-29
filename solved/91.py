import time
import helpers
import math

# inputFile = open('resources/', 'r')

start = time.perf_counter()

n = 50

a = n * n * 3
b = n // 2 * 2
c = a + b
others = 0
results = set()
for i in range(1, n + 1):
    for j in range(1, n + 1):
        f = i * i + j * j
        for k in range(0, n + 1):
            if k != j:
                j2t = (f - k * j) / i
                if j2t.is_integer() and n >= int(j2t) >= 0:
                    results.add(((i, j), (k, j2t)))

print(c)
print(a + len(results))
print(time.perf_counter() - start)
