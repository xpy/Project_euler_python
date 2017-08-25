import time
import helpers
import math

# inputFile = open('resources/', 'r')

start = time.clock()

summa = 0
top = 5
done = {}


def asdf(top):
    global summa
    for i in range(top, 1, -1):
        a = top // i
        done[top] = True
        summa += 1
        print('a', top, a)
        print('summa', summa)
        if top - a > 1 and not done.get(top - a, False):
            asdf(top - a)


# asdf(top)
print(math.factorial(5 + 2 - 1) / (math.factorial(5) * math.factorial(2 - 1)))
import itertools

count = 0
aaaaa = set()
ss_collection = []
for i in itertools.product(['0', 'X'], repeat=10):
    count += 1
    if i not in aaaaa and tuple(reversed(i)) not in aaaaa:
        s0 = 0
        ss = {}
        for j in i:
            if j == '0':
                s0 += 1
            elif s0 > 0:
                ss[s0] = ss.get(s0, 0) + 1
                s0 = 0
        if s0 > 0:
            ss[s0] = ss.get(s0, 0) + 1
        if ss not in ss_collection:
            ss_collection.append(ss)
            # print(i, ss)
            aaaaa.add(i)
            # print(count, i)
print((count - 2) / 2)
for i in sorted(aaaaa):
    print(i)
print(len(aaaaa))
print(time.clock() - start)
