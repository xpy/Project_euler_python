import time
import helpers
import math
import copy

import sys

# sys.setrecursionlimit(5000)
print("\033[0;35msys.getrecursionlimit()", sys.getrecursionlimit(), "\033[0m")

inputFile = open('resources/matrix.txt', 'r')

arr = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331]
]

arr = [[int(n) for n in l.split(',')] for l in inputFile]

w = len(arr[0])
h = len(arr)

the_cache_thing = []
for i in range(0, h):
    the_cache_thing.append([None for j in range(0, w)])
min_tail_sum = 9999999
# w = 80
# h = 80
head_num = 0

end = (w - 1, h - 1)

left_margin = 0
top_margin = 0


class Head:
    i = 0
    j = 0
    # tuple (i,j)
    dirs = {
        't': (-1, 0),
        'r': (0, 1),
        'b': (1, 0),
        'l': (0, -1)
    }
    dir_order = ['t', 'r', 'b', 'l']
    current_dir = -1

    tail = {}
    tail_set = set()
    tail_sum = 0

    def __init__(self, i, j, previous_head=None, previous_dir=None) -> None:
        global head_num, min_tail_sum
        self.i = i
        self.j = j
        self.head = head_num
        self.tail_sum = arr[i][j]
        head_num += 1
        if previous_head:
            self.tail = previous_head.tail.copy()
            self.tail[(previous_head.i, previous_head.j)] = previous_dir
            self.tail_set = set(self.tail.keys())
            self.tail_sum += previous_head.tail_sum
        if (i, j) == end:
            # print("\033[0;35mend", end, "\033[0m")
            if self.tail_sum < min_tail_sum:
                # print("\033[0;35mtail", self.tail, self.tail_sum, "\033[0m")
                min_tail_sum = self.tail_sum

    def get_next_move(self):
        self.current_dir += 1
        if self.current_dir == len(self.dir_order):
            return False
        next_step = self.get_next_valid_step()
        while next_step is False:
            self.current_dir += 1
            if self.current_dir == len(self.dir_order):
                return False
            next_step = self.get_next_valid_step()
        return next_step

    culprits = {
        't': ((-1, -1), (-1, 1)),
        'r': ((-1, 1), (1, 1)),
        'b': ((1, -1), (1, 1)),
        'l': ((-1, -1), (1, -1)),
    }

    def get_next_valid_step(self):
        next_dir = self.dirs[self.dir_order[self.current_dir]]
        next_step = (self.i + next_dir[0], self.j + next_dir[1])
        if (not (left_margin <= next_step[0] < w)) or \
                (not (top_margin <= next_step[1] < h)) or next_step in self.tail_set:
            return False
        return next_step

    def do_next_move(self):
        global min_tail_sum
        next_move = self.get_next_move()
        while next_move:
            next_sum = self.tail_sum + arr[next_move[0]][next_move[1]]
            if the_cache_thing[next_move[0]][next_move[1]] is None:
                the_cache_thing[next_move[0]][next_move[1]] = next_sum
            if isinstance(the_cache_thing[next_move[0]][next_move[1]], Head):
                cache_sum = the_cache_thing[next_move[0]][next_move[1]].tail_sum
            else:
                cache_sum = the_cache_thing[next_move[0]][next_move[1]]
            if next_sum <= cache_sum and next_sum < min_tail_sum:
                next_head = Head(next_move[0], next_move[1], self, self.current_dir)
                the_cache_thing[next_move[0]][next_move[1]] = next_head
                next_head.do_next_move()
            next_move = self.get_next_move()


start_time = time.clock()
or_w = w
or_h = h

w = 2
h = 2
a = Head(0, 0)
a.do_next_move()
the_cache_thing[0][0] = a
for i in range(1, or_w - 1):
    w = i + 2
    h = i + 2
    end = (w - 1, h - 1)
    # print("\033[0;35mthe_cache_thing", the_cache_thing, "\033[0m")
    for j in range(0, i):
        if isinstance(the_cache_thing[j][i], int) or the_cache_thing[j][i] is None:
            print("\033[0;35m'fuck'", 'fuck', "\033[0m")
            continue
        the_cache_thing[j][i].current_dir = -1
        the_cache_thing[j][i].do_next_move()
        try:
            min_tail_sum = min(min_tail_sum + arr[end[0]][end[1] + 1],
                               min_tail_sum + arr[end[0] + 1][end[1]])
            min_tail_sum += arr[end[0] + 1][end[1] + 1]
        except IndexError:
            pass
        end = (w - 1, h - 1)
        if isinstance(the_cache_thing[i][j], int) or the_cache_thing[i][j] is None:
            print("\033[0;35m'fuck'", 'fuck', "\033[0m")
            continue
        the_cache_thing[i][j].current_dir = -1
        the_cache_thing[i][j].do_next_move()
        try:
            min_tail_sum = min(min_tail_sum + arr[end[0]][end[1] + 1],
                               min_tail_sum + arr[end[0] + 1][end[1]])
            min_tail_sum += arr[end[0] + 1][end[1] + 1]
        except IndexError:
            pass
print(the_cache_thing[w - 1][h - 1].tail_sum)
print(time.clock() - start_time)
