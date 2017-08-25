import time
import helpers
import math

# inputFile = open('resources/', 'r')

start = time.clock()

summa = 0
top = 5
done = {}

import time
import helpers
import math

# inputFile = open('resources/', 'r')

start = time.clock()

maximum = 5

pres = 1
prediff = 0
for maximum in range(1, 150):
    coins = list(reversed([i for i in range(1, maximum + 1)]))
    l = len(coins)


    def makeSum(summa, index):
        variations = 0
        for i in range(index, l):
            coin_sum = summa + coins[i]
            if coin_sum < maximum:
                variations += makeSum(coin_sum, i)
            elif coin_sum == maximum:
                variations += 1
        return variations


    s = makeSum(0, 0)
    print(maximum, s, s - pres, s - pres - prediff)
    prediff = s - pres
    pres = s

print(time.clock() - start)
# asdf(top)
print(time.clock() - start)
