import time
import helpers
import math

inputFile = open('resources/p082_matrix.txt', 'r')

mmap = [[int(n) for n in l.split(',')] for l in inputFile]

start = time.clock()

w = 80
h = 80

new_map = [[0] + [0 for _ in range(w)] for _ in range(h)]
for j in range(1, w+1):
    for i in range(0, h):
        new_map[i][j] = mmap[i][j-1] + new_map[i][j-1]
    for i in range(1, h):
        new_map[i][j] = min(new_map[i][j], mmap[i][j-1] + new_map[i - 1][j])
    for i in range(h - 2, -1, -1):
        new_map[i][j] = min(new_map[i][j], mmap[i][j-1] + new_map[i + 1][j])

minimum = math.inf
for i in range(0, h):
    minimum = min(minimum, new_map[i][h])

print('---', minimum)
print(time.clock() - start)
