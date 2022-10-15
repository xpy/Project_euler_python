import time
import helpers

start = time.perf_counter()

primes = [i for i in helpers.primes_to(9999) if (i > 1000)]
results = []

for index, prime in enumerate(primes):
    for prime2 in primes[index + 1:]:
        if helpers.is_permutation(prime, prime2):
            prime3 = prime2 + prime2 - prime
            if helpers.is_permutation(prime, prime3) and prime3 in primes:
                results.append([prime, prime2, prime3])

print(results)

print('-' * 20)
print(time.perf_counter() - start)
