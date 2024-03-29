import time
import helpers

start = time.perf_counter()
num = 1
increment = 2
numCount = 1
numOfPrimes = 0
while True:
    for j in range(0, 4):
        num += increment
        numCount += 1
        if helpers.is_prime(num):
            numOfPrimes += 1
    if float(numOfPrimes) / float(numCount) < .1:
        break
    increment += 2
print(increment + 1)  # 26241

print('-' * 20)
print(time.perf_counter() - start)
