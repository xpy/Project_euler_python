import time
import helpers
import math
import itertools

# inputFile = open('resources/', 'r')

start = time.clock()


def root(a, b, c):
    return int(helpers.roots_2(a, b, c))


start_num = 1000
end_num = 9999

triangles = [helpers.triangle(i) for i in range(root(1, -1, start_num * 2) + 1, root(1, -1, 2 * 9999))]
squares = [helpers.square(i) for i in range(int(start_num ** .5) + 1, int(end_num ** .5))]
pentagonals = [helpers.pentagonal(i) for i in range(root(3, -1, start_num * 2) + 1, root(3, -1, 2 * end_num))]
hexagonals = [helpers.hexagonal(i) for i in range(root(2, -1, start_num) + 1, root(2, -1, end_num))]
heptagonals = [helpers.heptagonal(i) for i in range(root(5, -3, 2 * start_num) + 2, root(5, -3, 2 * end_num))]
octagonals = [helpers.octagonal(i) for i in range(root(3, -2, start_num) + 1, root(3, -2, end_num))]


# print(triangles)
# print(squares)
# print(pentagonals)
# print(hexagonals)
# print(heptagonals)
# print(octagonals)
#
# print('=========================================')


def do_the_thing(list_list, iterations):
    if iterations == len(list_list):
        return list_list
    for fin, i in [(i % 100, i) for i in list_list[0]]:
        l = [j for j in list_list[1] if math.floor(j / 100) == fin and fin >= 10]
        ret = do_the_thing([l] + list_list[2:] + [[i]], iterations + 1) if len(l) else False
        if ret:
            return ret


res = []
for i in [list(i) for i in
          itertools.permutations([triangles, squares, pentagonals, hexagonals, heptagonals, octagonals], 6)]:
    res = (do_the_thing(i, 0))
    if res:
        print(res)
        break

print(sum([i[0] for i in res]))
print(time.clock() - start)
