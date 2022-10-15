import time
import helpers
import math

# inputFile = open('resources/', 'r')

start = time.perf_counter()
from decimal import *

getcontext().prec = 150
print(sum([(sum([int(digit) for digit in str(Decimal(i).sqrt() * (10 ** 100))[0:100]])) for i in [i for i in range(1, 101) if (i ** .5) != int((i ** .5))]]))
print(time.perf_counter() - start)
