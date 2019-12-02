import time
import helpers
import math

# inputFile = open('resources/', 'r')

start_time = time.clock()

s = sum(int(i) for i in str(pow(2, 1000)))
print("\033[0;35ms", s, "\033[0m")
print(time.clock() - start_time)
