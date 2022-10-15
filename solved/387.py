import time
import helpers
import math

# inputFile = open('resources/', 'r')

start_time = time.perf_counter()

hasdasdfs = set()
not_hasss = set()


def is_harshad(num):
    if num < 10 or num in hasdasdfs:
        return True
    if num in not_hasss:
        return False
    if num % sum([int(i) for i in str(num)]) == 0:
        return is_harshad(num // 10)
    return False


num = 1
hazards = {0: [1, 2, 3, 4, 5, 6, 7, 8, 9]}
results = []
for k in range(0, 12):
    hazards[k + 1] = []
    for h in hazards[k]:
        h *= 10
        for i in range(0, 10):
            hi = h + i
            if is_harshad(hi):
                hazards[k + 1].append(hi)
                if helpers.is_prime(hi / sum([int(ii) for ii in str(hi)])):
                    for p in range(0, 10):
                        the_num = hi * 10 + p
                        if helpers.is_prime(the_num):
                            results.append(the_num)
                    # print("\033[0;35mi", hi, "\033[0m")

print("\033[0;35msum(results)", sum(results), "\033[0m")
print(time.perf_counter() - start_time)
