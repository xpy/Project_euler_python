__author__ = 'xPy'
import time
start = time.clock()

from itertools import permutations
max = 9
divisors = [2, 3, 5, 7, 11, 13, 17]
results = []


def check(row):
    '''
    @type row: list
    '''
    for i, val in enumerate(row[1:-2]):
        if sum([j * 10 ** (2 - index) for index, j in enumerate(row[i + 1:i + 4])]) % divisors[i]:
            return False
    return True


for row in [i for i in permutations(range(0, max + 1), max + 1) if (i[0] > 0) and check(i)]:
    results.append(row)

print sum(map(lambda x: int(''.join(map(str, x))), results))

print '-' * 20
print time.clock() - start