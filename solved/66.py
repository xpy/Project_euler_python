import time
import helpers
import math

# inputFile = open('resources/', 'r')

start = time.clock()

# print(fraction(23))
num = 5


def find_minimal_solution(num):
    for i in helpers.convergents(num):
        if i[0] ** 2 - num * (i[1] ** 2) == 1:
            return i


max_n = 0
for i in [i for i in range(2, 1000) if not (i ** .5).is_integer()]:
    ms = find_minimal_solution(i)
    max_n = max(max_n, ms[0])
    if not ms:
        print('????????????????????????????')
    print(i, ms)

print('max_n', max_n)
print(time.clock() - start)
