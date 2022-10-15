import time
import helpers
import math

# inputFile = open('resources/', 'r')

start = time.perf_counter()

cubic_dict = dict()
last_key = 0
first_key = 0


def get_cubic_root(num):
    return round(num ** (1. / 3.))


# Very slow, don't even know if it works
def do_the_thing(number):
    global biggest_diff
    global cubic_dict
    global last_key
    global first_key

    target = 5

    number_root = get_cubic_root(number)
    if (number_root ** 3) != number:
        return False

    biggest_root = get_cubic_root(int(''.join(sorted(list(str(number)), reverse=True))))

    str_num = str(number)
    for key in range(first_key, number_root):
        if key in cubic_dict:
            del cubic_dict[key]
    first_key = number_root - 1

    if biggest_diff < (biggest_root - number_root):
        biggest_diff = biggest_root - number_root

    ordered_num = ''.join(sorted(list(str_num)))

    for i in range(last_key, biggest_root + 1):
        cubic_dict[i] = ''.join(sorted(list(str(i ** 3))))
    last_key = biggest_root
    return list(cubic_dict.values()).count(ordered_num) == target


biggest_diff = 0


def do_it(target=3):
    for digits in range(1, 20):
        base_num = int("1" * digits)
        original = {i: ''.join(sorted(list(str(i ** 3)))) for i in
                    range(get_cubic_root(base_num), get_cubic_root(base_num * 9))}
        fff = sorted(original.values())
        for index, i in enumerate(fff):
            flag = 1
            for j in range(1, target):
                if index + j >= len(fff) or fff[index + j] != i:
                    break
                else:
                    flag += 1
            if flag == target:
                return sorted([key ** 3 for key in original if original[key] == i])


print(do_it(5))

# for n in range(1, 1000000000):
#     if do_the_thing(n):
#         print('YAYYYY!!!')
#         print(n)
#         break

print(time.perf_counter() - start)
