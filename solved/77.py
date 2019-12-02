import time
import helpers
import math

# inputFile = open('resources/', 'r')

start = time.clock()

primes = list(reversed(helpers.shieve_primes_to(10000)))
l = len(primes)


def makeSum(maximum, summa, index):
    variations = 0
    for i in range(index, l):
        coin_sum = summa + primes[i]
        if coin_sum < maximum:
            variations += makeSum(maximum, coin_sum, i)
        elif coin_sum == maximum:
            variations += 1
    return variations


for i in [i for i in range(2, 1000)]:
    thingies = []
    res = makeSum(i, 0, 0)
    if res > 5000:
        print(i, res)
        break

print(time.clock() - start)
