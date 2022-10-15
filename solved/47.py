import time
import helpers

start = time.perf_counter()

primesList = helpers.primes_to(1000)
primeListLength = len(primesList)
print('Started!')


def get_distinct_prime_factors(num, res):
    start_index = primeListLength
    half_num = int(num / 2) + 1
    if half_num < primesList[primeListLength - 1]:
        for index, prime in enumerate(primesList):
            if prime >= half_num:
                start_index = index + 1
                break
    for prime in [prime for prime in primesList[start_index::-1] if not num % prime]:
        if prime not in res:
            res.append(prime)
        res = get_distinct_prime_factors(num / prime, res)
        break
    return res


k = 0
numOfDistinct = 4
count = 0
while count < numOfDistinct and k < 200000:
    k += 1
    if len(get_distinct_prime_factors(k, [])) == numOfDistinct:
        count += 1
    else:
        count = 0
else:
    print(k - numOfDistinct + 1)

print('-' * 20)
print(time.perf_counter() - start)
