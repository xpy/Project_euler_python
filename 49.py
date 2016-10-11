import time
import helpers

start = time.clock()

primes = [i for i in helpers.primesTo(9999) if (i > 1000)]
results = []

for index, prime in enumerate(primes):
    for prime2 in primes[index + 1:]:
        if helpers.isPermutation(prime, prime2):
            prime3 = prime2 + prime2 - prime
            if helpers.isPermutation(prime, prime3) and prime3 in primes:
                results.append([prime, prime2, prime3])

print(results)

print('-' * 20)
print(time.clock() - start)
