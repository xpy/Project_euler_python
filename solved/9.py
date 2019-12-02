import time
import helpers
import math

# inputFile = open('resources/', 'r')

start_time = time.clock()
max_val = 1000
counter = 0
things = []
other_things = set()

for i in range(2, max_val):
    if counter > max_val:
        break
    for j in range(1, i):
        if ((i + j) % 2) and helpers.are_relative_prime(i, j):
            counter += 1
            t = tuple(sorted([2 * i * j, i * i - j * j]))
            things.append(t[1])
            other_things.add(t)
            if counter > max_val:
                break

max_thing = max(things)
new_things = set(things)
for thing in other_things:
    new_thing = thing
    while new_thing[1] < max_thing:
        hyp = math.sqrt(new_thing[0] * new_thing[0] + new_thing[1] * new_thing[1])
        asd = hyp + new_thing[0] + new_thing[1]
        if asd == 1000:
            print("\033[0;35masd", hyp * new_thing[0] * new_thing[1], "\033[0m")
        new_things.add(new_thing)
        new_thing = (new_thing[0] + thing[0], new_thing[1] + thing[1])
print(time.clock() - start_time)

print("\033[0;35mmax_thing", max_thing, "\033[0m")
print("\033[0;35mnew_things", new_things, "\033[0m")
