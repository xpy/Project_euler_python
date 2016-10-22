def isPalindromic2(num):
    num = str(num)
    l = len(num) - 1
    for index, i in enumerate(num):
        if num[l - index] != i: return False
    return True


def isPalindromic(num):
    return


def shieve_primes_to(to):
    prime_set = [True for i in range(0, to)]
    i = 2
    while i < to:
        for j in range(i * 2, to, i):
            prime_set[j] = False
        i += 1
        while i < len(prime_set) and not prime_set[i]:
            i += 1

    return [index for index, i in enumerate(prime_set) if i][2:]


import math


def primesTo(to):
    odds = [2]
    flag = True
    prek = 0
    for cur in range(3, to, 2):
        if flag:
            sqrtCur = cur ** .5
            # if sqrtCur == int(sqrtCur):
            #     flag = False
            while odds[prek] < sqrtCur:
                prek += 1
        else:
            flag = True
        if flag:
            for i in range(0, prek + 1):
                if not cur % odds[i]:
                    flag = False
                    break
            else:
                odds.append(cur)
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


_check_point_ = 0


def check_point(num):
    global _check_point_
    if _check_point_ % num == 0:
        print(_check_point_)
    _check_point_ += 1
