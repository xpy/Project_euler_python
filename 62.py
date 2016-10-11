import time
import helpers
import math

# inputFile = open('resources/', 'r')

start = time.clock()

cubic_dict = dict()
last_key = 0
first_key = 0


def get_cubic_root(num):
    return round(num ** (1. / 3.))


def do_the_thing(number):
    global biggest_diff
    global cubic_dict
    global last_key
    global first_key

    target = 5
    if number % 1000000 == 0:
        print("=======================" + str(number))
        print(cubic_dict)

    number_root = get_cubic_root(number)
    if (number_root ** 3) != number:
        return False
    biggest_root = get_cubic_root(int(''.join(sorted(list(str(number)), reverse=True))))
    sumz = 0
    str_num = str(number)
    for key in range(first_key, number_root):
        if key in cubic_dict:
            del cubic_dict[key]

    first_key = number_root

    if biggest_diff < (biggest_root - number_root):
        biggest_diff = biggest_root - number_root
        print(str(number_root) + "  ----  " + str(biggest_root))
        print(str(number) + "  ----  " + str(biggest_root ** 3))
        print(biggest_diff)
        print("----------------------------")

    ordered_num = ''.join(sorted(list(str_num)))
    # for i in range(last_key, biggest_root + 1):
    #     print("NO KEYYYY")
    #     cubic_dict[i] = ''.join(sorted(list(str(i ** 3))))
    # last_key = biggest_root

    for i in range(number_root, biggest_root + 1):
        # other_num = str(i ** 3)
        if i > last_key:
            print("NO KEYYYY")
            cubic_dict[i] = ''.join(sorted(list(str(i ** 3))))
            last_key = i
        other_num = cubic_dict[i]
        if ordered_num == other_num:
            sumz += 1
    return sumz == target


biggest_diff = 0

for n in range(1, 1000000000):
    if do_the_thing(n):
        print('YAYYYY!!!')
        print(n)
        break

print(time.clock() - start)
