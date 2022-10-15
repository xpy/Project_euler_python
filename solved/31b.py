import time
import helpers
import math

# inputFile = open('resources/', 'r')

start = time.perf_counter()
coins = [1, 2, 5, 10, 20, 50, 100, 200]
target = 200


print(math.factorial(100 + 2 - 1)/(math.factorial(2 - 1) * math.factorial(100)))
print(math.factorial(50 + 4 - 1)/(math.factorial(4 - 1) * math.factorial(50)))
print(math.factorial(10 + 10 - 1)/(math.factorial(10 - 1) * math.factorial(10)))
print(math.factorial(5 + 10 - 1)/(math.factorial(10 - 1) * math.factorial(5)))
print(math.factorial(2 + 10 - 1)/(math.factorial(10 - 1) * math.factorial(5)))


print(time.perf_counter() - start)
