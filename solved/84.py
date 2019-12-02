import time
import helpers
import math
import itertools

# inputFile = open('resources/', 'r')

start_time = time.clock()
combination_chances = {}
p = list(itertools.product(range(1, 7), repeat=2))
all_chances = 0
for c in p:
    s = c[0] + c[1]
    combination_chances[s] = combination_chances.get(s, 0) + 1
    all_chances += 1

for index, c in combination_chances.items():
    combination_chances[index] = c / all_chances

print("\033[0;35mcombination_chances", combination_chances, "\033[0m")
print("\033[0;35mp", p, "\033[0m")
print("\033[0;35mlen(p)", len(p), "\033[0m")
combs = len(p)
squares = []

for i in range(0, 40):
    squares.append(combs)

squares[10] += squares[30]
squares[30] = 0

cc_chance = squares[1] / 16
squares[0] += cc_chance
squares[2] -= cc_chance

squares[10] += cc_chance
squares[2] -= cc_chance

squares[0] += cc_chance
squares[17] -= cc_chance

squares[10] += cc_chance
squares[17] -= cc_chance

squares[0] += cc_chance
squares[33] -= cc_chance

squares[10] += cc_chance
squares[33] -= cc_chance

ch_chance = squares[7] / 16
squares[0] += ch_chance * 3
squares[10] += ch_chance * 3
squares[11] += ch_chance * 3
squares[24] += ch_chance * 3
squares[39] += ch_chance * 3
squares[5] += ch_chance * 3

# go to next R
squares[15] += ch_chance
squares[25] += ch_chance
squares[5] += ch_chance
squares[15] += ch_chance
squares[25] += ch_chance
squares[5] += ch_chance

# go to next U
squares[12] += ch_chance
squares[28] += ch_chance
squares[12] += ch_chance

# Go back three squares
squares[4] += ch_chance
squares[19] += ch_chance
squares[33] += ch_chance

squares[7] -= ch_chance * 10
squares[22] -= ch_chance * 10
squares[36] -= ch_chance * 10

total = sum(squares)

i = 0
for sq in squares:
    chance = (sq * 100) / total
    for j in range(2, 13):
        sq_num = (i + j) % len(squares)
        squares[sq_num] += chance * combination_chances[j]

    i += 1
    total = sum(squares)


def find_the_thing():
    total = sum(squares)
    i = 0
    for sq in squares:
        print(i, ' ', sq, " ", (sq * 100) / total, '%')
        i += 1


find_the_thing()
total = sum(squares)
sq = squares[10]
print(10, ' ', sq, " ", (sq * 100) / total, '%')
sq = squares[25]
print(25, ' ', sq, " ", (sq * 100) / total, '%')
sq = squares[24]
print(24, ' ', sq, " ", (sq * 100) / total, '%')
sq = squares[0]
print(0, ' ', sq, " ", (sq * 100) / total, '%')

print(time.clock() - start_time)
