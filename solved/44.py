import time
import helpers

start = time.clock()
pentagonals = {}
k = 0
min_value = 10000000
results = []
while k < 1827555:
    pk = helpers.pentagonal(k)
    pentagonals[k] = pk
    for i in range(k - 1, 0, -1):
        # if i in pentagonals:
        pi = pentagonals[i]
        # else:
        #    i = helpers.pentagonal(i)
        iPk = pi + pk
        iMp = abs(pi - pk)
        if iMp > min_value:
            break
        if min_value > iMp and helpers.is_pentagonal(iPk):
            #  print iMp
            if helpers.is_pentagonal(iMp):
                print('*' * 20)
                print(iMp)
                if min_value > iMp:
                    results.append([[pi, pk], [i, k], iMp])
                    min_value = iMp

    k += 1
print('-' * 20)
for i in results:
    print(i)
print('-' * 20)
print(time.clock() - start)
