import time
import helpers
from itertools import product

start = time.clock()

f = open('resources\cipher1.txt', 'r')
letters = f.read().split(',')
letters = map(int, letters)
l = len(letters)
i = 0
passwords = list(product(range(97, 123), repeat=3))
for p in passwords:
    decyphered = ''
    flag = True
    i = 0
    while i < l:
        for letter in p:
            newLetter = letters[i] ^ letter
            if newLetter < 32 or newLetter > 122:
                flag = False
                break
            decyphered += chr(newLetter)
            i += 1
            if i == l:
                break
        if not flag:
            break
    else:
        print(sum(map(ord, decyphered)), end=' ')
        print(decyphered)
print('-' * 20)
print(time.clock() - start)
