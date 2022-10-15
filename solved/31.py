import time
import helpers
import math

# inputFile = open('resources/', 'r')

start = time.perf_counter()

coins = list(reversed([1, 2, 5, 10, 20, 50, 100, 200]))
maximum = 20
l = len(coins)


def makeSum(summa,  index):
    variations = 0
    for i in range(index, l):
        coin_sum = summa + coins[i]
        if coin_sum < maximum:
            variations += makeSum(coin_sum,  i)
        elif coin_sum == maximum:
            variations += 1
    return variations

print(makeSum(0, 0))

print(time.perf_counter() - start)
