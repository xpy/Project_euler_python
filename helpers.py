def isPalindromic2(num):
    num = str(num)
    l = len(num) - 1
    for index, i in enumerate(num):
        if (num[l - index] != i): return False
    return True


def isPalindromic(num):
    return


def primesTo(to):
    odds = [2]
    cur = 3
    flag = True
    numOfOdds = 0
    prek = 0
    while cur < to:
        if flag:
            sqrtCur = cur ** .5
            if sqrtCur == int(sqrtCur):
                flag = False
            for k in range(prek, numOfOdds):
                if odds[k] >= sqrtCur:
                    prek = k
                    break
        else:
            flag = True
        for i in range(0, prek):
            if not cur % odds[i] or not flag:
                flag = False
                break
        if flag:
            odds.append(cur)
            numOfOdds += 1
        cur += 2
    return odds


def isPermutation(str1, str2):
    str1 = list(str(str1))
    str2 = list(str(str2))
    str1.sort()
    str2.sort()
    return str1 == str2


def pentagonal(n):
    return n * (3 * n - 1) / 2


def isPentagonal(num):
    # delta = 1 + 24 * num
    # x1 = (1 + delta**.5) / 6
    x = (1 + (1 + 24 * num) ** .5) / 6
    # if x == int(x):
    #     print x , int(x),x == int(x)
    return x == int(x)


primes = []


def isPrime(num):
    global primes
    if num in primes:
        return True
    if num == 2:
        return True
    sqrt = num ** .5
    intSqrt = int(sqrt)
    if sqrt == intSqrt:
        return False
    for i in range(3, intSqrt + 1, 2):
        if num % i == 0:
            return False
    if not (num % 2 == 0):
        primes.append(num)
        return True


def areRelativePrime(a, b):
    minNum = min(a, b)
    maxNum = max(a, b)
    while minNum > 1:
        tmp = minNum
        minNum = maxNum % minNum
        maxNum = tmp
    return minNum == 1


def phi(num):
    # print [i for i in range(2,num) if areRelativePrime(num , i)]
    # if (isPrime(num)):
    #     return num - 1
    phiNum = 0
    phiCache = []
    for i in range(2, num):
        for j in phiCache:
            if i % j == 0:
                break
        else:
            if areRelativePrime(num, i):
                phiNum += 1
            else:
                phiCache.append(i)
    return phiNum + 1
    # return len([i for i in range(2,num) if areRelativePrime(num , i)])+1
