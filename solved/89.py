import time
from collections import OrderedDict

import helpers
import math

# inputFile = open('resources/', 'r')

start = time.clock()

letter_to_num = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000}


def silly_count(num):
    num = reversed(str(num))
    k = 1
    optimal_length = 0
    for i in num:
        to_add = 0
        if k == 4:
            to_add = int(i)
        elif i in ['1', '5']:
            to_add = 1
        elif i in ['2', '4', '6', '9']:
            to_add = 2
        elif i in ['3', '7']:
            to_add = 3
        elif i is '8':
            to_add = 4
        optimal_length += to_add
        k += 1
    return optimal_length


def parse_number(num):
    res = [0]
    new_num = 0
    for i in reversed(num):
        res.append(letter_to_num[i])
    for index, i in enumerate(res[1:]):
        new_num += i if i >= res[index] else -i
    return new_num


f = open('resources/roman.txt')

letters = 0
new_letters = 0
for l in f.readlines():
    l = l.replace('\n', '')
    parsed = parse_number(l)
    optimal = silly_count(parsed)
    print(l, parsed, len(l), optimal)
    letters += len(l)
    new_letters += optimal

print(letters, new_letters, letters - new_letters)
print(time.clock() - start)
