import time
from itertools import permutations

__author__ = 'xPy'

start = time.perf_counter()

max_value = 9
divisors = [2, 3, 5, 7, 11, 13, 17]


def check(row):
    """
    @type row: list
    """
    for i, val in enumerate(row[1:-2]):
        if sum([j * 10 ** (2 - index) for index, j in enumerate(row[i + 1:i + 4])]) % divisors[i]:
            return False
    return True


results = [i for i in permutations(range(0, max_value + 1), max_value + 1) if (i[0] > 0) and check(i)]

print(sum(map(lambda x: int(''.join(map(str, x))), results)))

print('-' * 20)
print(time.perf_counter() - start)
