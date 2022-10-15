import time
import helpers
import math

# inputFile = open('resources/', 'r')

start = time.perf_counter()

partitions = {0: 1, 1: 1}

other_thing = {}

limit = 1000000
skatoules = set()


def partition2(num):
    pa = 2
    if partitions.get(num, None) is not None:
        return partitions[num]
    summa = 0
    for i in range(1, num + 1):
        p = helpers.generalized_pentagonal2(i + 1)
        pn = num - p
        sign = 1 if pa % 4 > 1 else -1
        if pn >= 0:
            if partitions.get(pn, None) is None:
                partitions[pn] = partition2(pn)
            summa += sign * partitions[pn]
            pa += 1
        else:
            break

    return summa


def partition(num):
    if partitions.get(num, None) is not None:
        return partitions[num]
    summa = 0
    for i in range(1, num + 1):
        other = 1
        pn = 1
        summa = 0

        while pn > 0:
            if other_thing.get((other, i), None) is not None:
                ddd = other_thing[(other, i)]
                summa += ddd['summa']
                pn = ddd['pn']
                other += 1
                continue
            sum2 = 0
            p = helpers.generalized_pentagonal(other, 1)
            pn = i - p
            sign = 1 if other % 2 else -1
            if pn >= 0:
                sum2 += sign * partition(pn)
            p = helpers.generalized_pentagonal(other, -1)
            pn = i - p
            if pn >= 0:
                sum2 += sign * partition(pn)
            other_thing[(other, i)] = {'summa': sum2, 'pn': pn}
            summa += sum2
            other += 1
    partitions[num] = summa % limit
    return summa


k = 0

# print(partition2(vvvvv))
# print(skatoules)
# print(partitions)

while partition2(k) % limit != 0:
    if k % 1000 == 0:
        print(k, partition2(k))
        print(len(partitions))
        print(time.perf_counter() - start)
        if k % 100000 == 0:
            print("WE GOT 100000!!!", k, partition2(k))

    k += 1
print(k, partition2(k))

print(time.perf_counter() - start)
# asdf(top)
# 24061467864032622473692149727991
# 3000 496025142797537184410324879054927095334462742231683423624 66.
