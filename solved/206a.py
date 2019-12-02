import time
import helpers
import math
import itertools

# inputFile = open('resources/', 'r')

start = time.clock()

k = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
max_num = 1929394959697989990
nums = []
c = 1
for i in range(10 ** c, 10 ** (c + 1)):
    ii = list(str(i ** 2))
    if ii[-2 * c:][::-2] == k[-1 * c:]:
        nums.append(i)

c += 1
found = False
for c in range(2, 8):
    nums2 = set()
    for j in sorted(list(nums)):
        brk = False
        j10 = (10 ** len(str(j)))
        for i in range(1, 100):
            asdf = (i * j10 + j)
            asfsq = asdf ** 2
            if asfsq > max_num:
                if i == 1:
                    brk = True
                break
            ii = list(str(asfsq))
            check = ii[len(str(asdf)) * -1:][::-2][::-1]
            if check == k[-1 * len(str(asdf)) // 2:]:
                if len(check) == 5:
                    if ii[::2] == k:
                        print('AAAAAAAAAAAA', asdf)
                        found = True
                        break
                nums2.add(asdf)
        if found or brk:
            break
    if found:
        break
    # print('nums', nums)
    # print('nums2', sorted(list(nums2)))
    nums = nums2
# 1389019170

print(time.clock() - start)
