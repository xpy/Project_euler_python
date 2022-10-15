import time
import helpers
import math

# inputFile = open('resources/', 'r')

start = time.perf_counter()


def fibonachi_to(num):
    if num in [0, 1]:
        return 1
    else:
        return fibonachi_to(num - 1) + fibonachi_to(num - 2)


to = 500000
# 2011026
fibs = [1, 1]
counter = 2
lll = 500
ten9 = 10 ** 9
digits = [str(i) for i in range(1, 10)]
pre_tail = 1
tail = 1
for i in range(2, to):
    counter += 1
    next_fib = sum(fibs)
    new_tail = (tail + pre_tail) % 1000000000
    tail_set = sorted(str(new_tail))
    if tail_set == digits:
        print("!!!!!!!", counter, tail_set, next_fib)
        tip = next_fib // max(1, int(10 ** (math.floor(math.log10(next_fib)) + 1 - 9)))
        tip_set = sorted((str(tip)))
        # str_thing = str(next_fib)
        # tip_set = set(str(str_thing[:9]))
        if tip_set == digits:
            print("?????", counter, tip_set, next_fib)
            print('AMAZING!!!!', counter, next_fib)
            break
    pre_tail, tail = tail, new_tail
    fibs = [fibs[1], next_fib]

print(time.perf_counter() - start)
