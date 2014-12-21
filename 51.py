import time
import helpers

start = time.clock()
print 0b100 & 0b110
# helpers.primesTo(1000000)
# print([prime for prime in helpers.primesTo(1000000) if prime > 100000])
print '-' * 20
print time.clock() - start