import time
import helpers
import math

start = time.clock()

sequence = []
num_of_sequences = 0


def fraction_to(num, to=0, a=None, m=0, d=1):
    global num_of_sequences
    a = int(math.sqrt(num)) if not a else a
    next_m = d * a - m
    next_d = int((num - next_m ** 2) / d)
    next_a = int((int(math.sqrt(num)) + next_m) / next_d)
    # print(next_a, next_m, next_d, )
    sequence.append(next_a)
    if len(sequence)-1 % 2 == 0 and len(sequence) > 1:
        print(sequence)
        if sequence[1:len(sequence)-1 // 2] == sequence[len(sequence)-1 // 2:]:
            if len(sequence) // 2 % 2:
                num_of_sequences += 1
                print('AAAAAAAAAA')
            return
    if to > 0:
        fraction_to(num, to - 1, next_a, next_m, next_d)


for i in range(2, 14):
    if i ** .5 % 2:
        fraction_to(i, 100)

print(num_of_sequences)
print(time.clock() - start)
