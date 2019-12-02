import time
import helpers
import math
import itertools

# inputFile = open('resources/', 'r')

start = time.clock()
sums_map = {}
valid_sets = []

for i in itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3):
    s = sum(i)
    sums_map[s] = sums_map.get(s, []) + [i]

for i in sums_map:
    if len(set([k for j in sums_map[i] for k in j])) == 10:
        valid_sets.append(sums_map[i])


def is_valid(row):
    numbers = {1: {i: 0 for i in range(1, 11)}, 2: {i: 0 for i in range(1, 11)}}

    for i in row:
        numbers[1][i[1]] += 1
        numbers[2][i[2]] += 1
        if numbers[1][i[1]] >= 2 or numbers[2][i[2]] >= 2:
            return False
    return True


the_amazing_sets = []


def find_thingy(row, start_index, sets):
    for i in range(start_index, len(row)):
        if len(sets) == 0 or (row[i][0] not in [s for s2 in sets for s in s2] \
                                      and row[i][1] not in [s[0] for s in sets] \
                                      and row[i][2] not in [s[0] for s in sets]) \
                :
            sets.append(row[i])
            find_thingy(row, i, sets)
        if len(sets) == 5:
            if is_valid(sets):
                the_amazing_sets.append(sets.copy())
            break
    if len(sets):
        sets.pop()


for vss in valid_sets:
    find_thingy(vss, 0, [])

for amazing_set in the_amazing_sets:
    print(amazing_set)
print(time.clock() - start)
6357528249411013
6531031914842725
