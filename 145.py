import time
import helpers
import math

# inputFile = open('resources/', 'r')


start_time = time.clock()
results = set()
i = 10
maxa = 0
while i < 10 ** 9:
    if i % 1000000 == 0:
        print(i)
    if i % 10:
        str_sum = str(i + int(str(i)[::-1]))
        j = 0
        for s in str_sum[::-1]:
            if int(s) % 2 == 0:
                if j > 0:
                    stri = str(i)
                    itrs = stri[::-1]
                    l = len(stri)
                    fix = 1 if l % 2 == 0 else 0
                    if (l / 2) - fix > j:
                        rpart = stri[-j:]
                        lpart = itrs[-j:]
                        target = 10 ** len(lpart)
                        begin = (int(rpart) + int(lpart)) % target
                        i += target - begin
                break
            j += 1
        else:
            # print(i)
            start = 0
            results.add(i)
    i += 1
    # print(i, start)

print(sorted(results))

print("----", len(results))

print(time.clock() - start_time)
