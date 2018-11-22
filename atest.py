import time

import itertools

import helpers
import math

# inputFile = open('resources/', 'r')
target = 1000000

start = time.clock()
from math import gcd

n = int(input())

count = n**2

count+= int(n**2/2)

for i in range(1,n+1):
    for j in range(i):
        if (i,j)!=(0,0):
            if j==0:
                count+=2*n
            else:
                g = gcd(i,j)
                xstep = j//g
                ystep = i//g
                t = min(i//xstep,(n-j)//ystep)
                count+=(2*t)
                s = min(j//ystep,(n-i)//xstep)
                count+=(2*s)
print(count)

print(time.clock() - start)

