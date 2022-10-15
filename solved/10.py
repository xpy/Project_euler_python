import time
import helpers
import math

# inputFile = open('resources/', 'r')

start_time = time.perf_counter()

s = sum(helpers.shieve_primes_to(2 * (10 ** 6)))
print("\033[0;35ms", s, "\033[0m")
print(time.perf_counter() - start_time)
