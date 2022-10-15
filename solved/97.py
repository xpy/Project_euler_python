import time
import helpers

start = time.perf_counter()

starts = {}
num = ''
k = 0
power = 7830457
digits = 10

while len(num) < digits:
    k += 1
    num = str(2 ** k)
else:
    startNum = num
    numPower = k

'''
while len(num) <= digits:
    num = str(2 ** k)
    numLen = len(num)
    if numLen not in starts:
        starts[numLen] = {}
        starts[numLen]['start'] = num
        starts[numLen]['power'] = k
    k += 1

#print 2**power
#92596709376
# for i in starts:

i=10
for j in range(1,power+1):
    # print str(int(starts[i]['start'])*(2**j))[i*-1:]
    poweredNum = str(int(starts[i]['start'])*(2**j))
    # print poweredNum
    # print poweredNum[i*-1:]
    if poweredNum[i*-1:] == starts[i]['start']:
        print i, j
        lastDigits = int(starts[i]['start'])
        for k in range(0,((power-int(starts[i]['power']))%j)):
            lastDigits = str(int(lastDigits)*2)[i*-1:]
        print lastDigits
        # print '+' * 20
        break
else:
'''

mask = 10 ** digits
lastDigits = int(startNum)
for k in range(0, (power - int(numPower)) % power):
    lastDigits = (lastDigits + lastDigits) % mask
print(int(lastDigits) * 28433 + 1 % mask)

# 10
# 9700303872
# 275808739992577

# 11
# 39700303872
# 1128798739992577

# 12
# 839700303872
# 23875198739992577

# 8639992577


print('+' * 20)

print('-' * 20)
print(time.perf_counter() - start)
