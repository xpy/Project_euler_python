import time
import helpers
import math

start = time.perf_counter()

num_of_sequences = 0


def fraction_to(num, to=0, a=None, m=0, d=1):
    global num_of_sequences, sequence_length, truples
    a = a if a else int(math.sqrt(num))
    truple = (a, m, d)
    next_m = d * a - m
    next_d = int((num - next_m ** 2) / d)
    next_a = int((int(math.sqrt(num)) + next_m) / next_d)
    if truple in truples:
        num_of_sequences += sequence_length % 2
        # if sequence_length % 2 == 0:
        #     # print('LOOOOOP', num)
        #     # print(num, sequence)
        #     # print('-' * 5)
        #     num_of_sequences += 1
        return
    truples.add(truple)
    # sequence.append(next_a)
    sequence_length += 1
    if to > 0:
        fraction_to(num, to - 1, next_a, next_m, next_d)


# params = set()
# sequence = []
# fraction_to(23, 100)

for i in range(2, 10000):
    if i ** .5 != int(i ** .5):
        truples = set()
        sequence = []
        sequence_length = 1
        fraction_to(i, 20000)

print(num_of_sequences)
print(time.perf_counter() - start)
