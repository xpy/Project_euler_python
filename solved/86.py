import time
import helpers
import math
from decimal import *
import itertools

# inputFile = open('resources/', 'r')

start_time = time.clock()
num_of_nums = 0
counter = 0
things = []
other_things = set()
mapi = {}
max_num = 1000000
flag = max_num // 1000
# num_of_nums 10153 210 420

for i in range(2, flag):
    if counter > flag:
        break
    for j in range(1, i):
        if ((i + j) % 2) and helpers.are_relative_prime(i, j):
            counter += 1
            t = tuple(sorted([2 * i * j, i * i - j * j]))
            things.append(t[1])
            other_things.add(t)
            if counter > flag:
                break

print("\033[0;35m'?????'", '?????', "\033[0m")
max_thing = max(things)
new_things = set(things)
for thing in other_things:
    new_thing = thing
    while new_thing[1] < max_thing:
        new_things.add(new_thing)
        new_thing = (new_thing[0] + thing[0], new_thing[1] + thing[1])

k = 1
print("\033[0;35m'!!!!!'", '!!!!!', "\033[0m")

# print("\033[0;35mother_things", sorted(new_things), "\033[0m")

while k < max_num:
    k += 1
    k2 = k // 2
    for i in range(1, k + 1):
        q = i if i <= k2 else k - i + 1
        if tuple(sorted([k, i * 2])) in new_things:
            num_of_nums += q
        if tuple(sorted([k, i * 2 + 1])) in new_things and i < k:
            num_of_nums += q - (1 if i > k2 else 0)
    if num_of_nums > max_num:
        break

print("\033[0;35mnum_of_nums", num_of_nums, k, "\033[0m")

print(time.clock() - start_time)
