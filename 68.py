import time
import helpers
import math
import itertools

# inputFile = open('resources/', 'r')

start = time.clock()
sadf = {}
# l = (itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
for i in itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3):
    s = sum(i)
    if not sadf.get(s):
        sadf[s] = []
    sadf[s].append(i)
valid_sets = {}
for i in sadf:
    s = set()
    for j in sadf[i]:
        for k in j:
            s.add(k)
    if len(s) == 10:
        valid_sets[i] = (sadf[i])
for vss in valid_sets:
    l = len(valid_sets[vss])
    for i in range(0, l):
        first_set = valid_sets[vss][i]
        for j in range(i, l):
            if valid_sets[vss][j][0] not in first_set and valid_sets[vss][j][2] not in first_set and valid_sets[vss][j][
                1] == first_set[2]:
                second_set = valid_sets[vss][j]
                print(first_set,second_set)
print(time.clock() - start)
