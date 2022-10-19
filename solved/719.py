import time
import helpers
import math
from itertools import tee, zip_longest

# inputFile = open('resources/', 'r')

start_time = time.perf_counter()


def do_the_sum(num):
    return sum([int(x) for x in str(num)])


def do_all_the_sums(num):
    new_sum = do_the_sum(num)
    if new_sum >= 10:
        return do_all_the_sums(new_sum)
    return new_sum


indices_map = {}


def get_indices(numa, padding):
    if (numa, padding) in indices_map:
        return indices_map[(numa, padding)]
    indices_list = [0]
    bin_m = "{0:b}".format(numa).rjust(padding, '0')
    for index in range(len(bin_m)):
        if bin_m[index] == '1':
            indices_list.append(index + 1)
    # if numa in indices_map:
    #     print('found?', numa, bin_m, indices_list, indices_map[numa])
    indices_map[(numa, padding)] = indices_list
    return indices_map[(numa, padding)]


result = 0
limit = pow(10, 9)
num = 0
pow_i = 0
while pow_i < limit:
    num += 9
    for i in [0, 1]:
        new_num = num + i
        pow_i = new_num * new_num
        str_pow = str(pow_i)
        l = len(str_pow) - 1
        for m in range(0, pow(2, l)):
            indices = get_indices(m, l)
            parts = [str_pow[i:j] for i, j in zip(indices, indices[1:] + [None])]
            sum_of_parts = sum([int(part) for part in parts])
            if sum_of_parts == new_num:
                print(pow_i, '----', indices, parts, sum_of_parts)
                print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                result += pow_i
                break
print('=================', result)
print(time.perf_counter() - start_time)
