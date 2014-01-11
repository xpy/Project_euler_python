import time
import helpers

start = time.clock()
pentagonals = {}
k = 0
min = 10000000
results = []
while (k < 1827555):
    pk = helpers.pentagonal(k)
    pentagonals[k] = pk
    for i in range(k - 1, 0, -1):
        #if i in pentagonals:
        pi = pentagonals[i]
        #else:
        #    i = helpers.pentagonal(i)
        iPk = pi + pk
        iMp = abs(pi - pk)
        if iMp > min: break
        if min > iMp and  helpers.isPentagonal(iPk):
        #  print iMp
            if helpers.isPentagonal(iMp):
                print '*' * 20
                print (iMp)
                if min > iMp:
                    results.append([[pi, pk], [i, k], iMp])
                    min = iMp

    k += 1
print '-' * 20
for i in results:
    print i
print '-' * 20
print time.clock() - start