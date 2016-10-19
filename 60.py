import time
import helpers
import math

# inputFile = open('resources/', 'r')

start = time.clock()
primes = helpers.primesTo(100000)
l = [3]


def do_the_thing(pr1, pr2):
    return int(str(pr1) + str(pr2)) in primes and int(str(pr2) + str(pr1)) in primes

k = 0
for prime in primes :
    if k % 1000 == 0:
        print(k)
    k+=1
    for prime2 in l:
        if not do_the_thing(prime, prime2):
            l.append(prime)
            break

print(l)
print(time.clock() - start)
