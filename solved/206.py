import time
import helpers
import math
from itertools import product

# inputFile = open('resources/', 'r')

start = time.perf_counter()

a = '1234567890'


def check_num(prea):
    for i in range(1, 9999999999999999):
        num = str(i) + prea
        if int(num) > 1389026624:
            return False
        num_to_check = str(int(num) ** 2)[::-2][::-1]
        if num_to_check == a[-len(num_to_check):]:
            if len(num_to_check) == 10:
                print(num, list(num_to_check), a[-len(num_to_check):])
                return True
            if check_num(num):
                return True
    return False


check_num('0')

print(time.perf_counter() - start)
# 1929374254627488900 1389019170
# 1929374254627488900
