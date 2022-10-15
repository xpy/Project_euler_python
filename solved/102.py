import time
import helpers
import math

# inputFile = open('resources/', 'r')

start = time.perf_counter()

f = open('resources/triangles.txt')


def test_the_thing(a, b, c):
    [x1, y1], [x2, y2], [xt, yt] = a, b, c
    return (xt - x1) * (y2 - y1) - (yt - y1) * (x2 - x1)


num_of_triangles = 0
for i in f.readlines():
    i = i.replace('\n', '')
    i = [int(j) for j in i.split(',')]
    i = [i[j:j + 2] for j in range(0, len(i), 2)]
    is_in = True
    for j in range(0, 3):
        ja = j % 3
        jb = (j + 1) % 3
        jc = (j + 2) % 3
        other = test_the_thing(i[ja], i[jb], i[jc])
        center = test_the_thing(i[ja], i[jb], [0, 0])
        is_in &= other * center > 0
        print(other, center, other * center > 0)
    if is_in:
        num_of_triangles += 1
    print('---------------------', is_in)

print(num_of_triangles)
print(time.perf_counter() - start)
