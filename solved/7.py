import time
import helpers
import math

# inputFile = open('resources/', 'r')

start_time = time.perf_counter()

print(helpers.shieve_primes_to(1000000)[10000])
print(time.perf_counter() - start_time)
