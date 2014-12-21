import time
import helpers

start = time.clock()


def phi3(num):
    # print [i for i in range(2,num) if areRelativePrime(num , i)]
    # if (helpers.isPrime(num)):
    #     return -1
    global maxPhi
    phiNum = 1
    nums = range(2, num)
    numsLen = len(nums)
    flag = True
    while flag:
        flag = False
        for i in nums:
            if helpers.areRelativePrime(num, i):
                phiNum += 1
                if (num / phiNum) <= maxPhi:
                    return -1
            else:
                nums = [j for j in nums if ((j % i) > 0) and j >= i]
                numsLen = len(nums)
                flag = True
                break
    return phiNum


def phi2(num):
    # print [i for i in range(2,num) if areRelativePrime(num , i)]
    if (helpers.isPrime(num)):
        return -1
    global maxPhi
    phiNum = 1
    phiCache = []
    for i in range(2, num):
        for j in phiCache:
            if i % j == 0:
                break
        else:
            if helpers.areRelativePrime(num, i):
                phiNum += 1
                if (num / phiNum) <= maxPhi:
                    return -1
            else:
                phiCache.append(i)
    return phiNum


maxPhi = 0
maxNi = 0
for i in range(2, 10000):
    if (i % 1000) == 0:
        print i
    phiNum = phi3(i)
    if phiNum > 0:
        phiDiv = float(i) / phiNum
        if phiDiv > maxPhi:
            maxPhi = phiDiv
            maxNi = i
            print i, phiNum, phiDiv

print maxPhi, maxNi
print '-' * 20
print time.clock() - start