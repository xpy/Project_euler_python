import time
from decimal import Decimal

import helpers
import math

# inputFile = open('resources/', 'r')

start_time = time.clock()

max_num = int((10 ** 9) / 3)
# max_num = 1000
# sss = 0
# for i in range(1, max_num, 4):
#     s = (3 * i + 1) / 2
#     si = s - i
#     area = Decimal(s * (si ** 2) * (si - 1)).sqrt()
#     # area = Decimal(8 * (i ** 4) * ((i + 1) ** 2) - (2 * i * i + (i - 1) * i) ** 2).sqrt()/4
#     if area == int(area):
#         print("\033[0;35mi, area", i, area, "\033[0m")
#         sss += s * 2
#         print("\033[0;35msss", sss, "\033[0m")
#     if i % 100001 == 0:
#         print("\033[0;35mi", i, "\033[0m")
s = 0
for i in range(2, max_num):
    sqi = i * i
    sqii = (sqi - 1) / 3
    sqrtii = pow(sqii, .5)
    if sqrtii == int(sqrtii):
        c = sqrtii + sqi
        per = c * 3 + 1
        if per > (10 ** 9):
            break
        s = per / 2
        area = Decimal(s * (s - c) * (s - c) * (s - (c + 1))).sqrt()
        print("\033[0;35msqrtii", c, "\033[0m")
        if area == int(area):
            print("\033[0;35mi, area", i, area, "\033[0m")
        # print("\033[0;35mi, area",s, area, "\033[0m")
        s += per
    # for j in range(1, i):
    #     sqj = j * j
    #     # c = sqi + sqj
    #     # a = sqi - sqj`
    #     if sqj == sqii:
    #         print("\033[0;35mc", sqi + sqj, "\033[0m")
print("\033[0;35ms", s, "\033[0m")
print(time.clock() - start_time)
