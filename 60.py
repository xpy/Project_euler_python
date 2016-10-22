import time
import helpers
import math

# inputFile = open('resources/', 'r')

start = time.clock()
primes = [str(i) for i in helpers.shieve_primes_to(90000000)]
primesSet = set(primes)
print('PRIMES RRREADY!!!')
print(time.clock() - start)

# len_primes = {}
# for i in primes:
#     len_primes[len(i)] = set()
# for i in primes:
#     len_primes[len(i)] |= {i}
# l = {}
# for i in primes:
#     l[i] = []
biggest_len = len(primes[-1])
print('INDEXES RRREADY!!!')
print(biggest_len)
print(time.clock() - start)


def check(sub_list, target_length):
    # print(sub_list)
    if target_length == 0:
        return sub_list[0]
    if len(sub_list) < target_length:
        return False
    for j in range(1, len(sub_list)):
        if len(sub_list[j]) * 2 > biggest_len:
            return False
        res = []
        for i in sub_list[j:]:
            if len(i + sub_list[j - 1]) > biggest_len:
                break
            if do_the_thing(i, sub_list[j - 1]):
                res.append(i)
        if len(res) >= target_length:
            chk = check(res, target_length - 1)
            if chk:
                chk.append(sub_list[j - 1])
                return chk

    return False


def do_the_thing(pr1, pr2):
    return pr1 + pr2 in primesSet and pr2 + pr1 in primesSet


# ['8389', '6733', '5701', '5197', '13']
# print(check(['673', '613', '529', '499', '457', '397', '199', '109', '7', '3'], 3))
print(check(primes, 4))

print(time.clock() - start)
