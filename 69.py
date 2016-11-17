import time
import helpers

start = time.clock()


def phi3(num):
    # print [i for i in range(2,num) if areRelativePrime(num , i)]
    # if (helpers.isPrime(num)):
    #     return -1
    global maxPhi
    phi_num = 1
    nums = range(2, num)
    flag = True
    while flag:
        flag = False
        for i in nums:
            if helpers.are_relative_prime(num, i):
                phi_num += 1
                if (num / phi_num) <= maxPhi:
                    return -1
            else:
                nums = [j for j in nums if ((j % i) > 0) and j >= i]
                flag = True
                break
    return phi_num


def phi2(num):
    # print [i for i in range(2,num) if areRelativePrime(num , i)]
    if helpers.is_prime(num):
        return -1
    global maxPhi
    phi_num = 1
    phi_cache = []
    for i in range(2, num):
        for j in phi_cache:
            if i % j == 0:
                break
        else:
            if helpers.are_relative_prime(num, i):
                phi_num += 1
                if (num / phi_num) <= maxPhi:
                    return -1
            else:
                phi_cache.append(i)
    return phi_num


maxPhi = 0
maxNi = 0
for i in range(2, 10000):
    if (i % 1000) == 0:
        print(i)
    phiNum = phi3(i)
    if phiNum > 0:
        phiDiv = float(i) / phiNum
        if phiDiv > maxPhi:
            maxPhi = phiDiv
            maxNi = i
            print(i, phiNum, phiDiv)

print(maxPhi, maxNi)
print('-' * 20)
print(time.clock() - start)
