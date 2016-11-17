import time
import helpers
import math

start = time.clock()

print(max([(nums[1] * math.log10(nums[0]), i + 1) for i, nums in
           enumerate([map(int, line.split(',')) for line in open('resources/base_exp.txt').readlines()])]))
'''
maxNum = 0
maxIndex = 0
index = 0
for nums in [map(int,line.split(',')) for line in  base_exp.readlines()]:
    index+=1
    res =nums[1]*math.log10(nums[0])
    if(res > maxNum):
        maxNum= res
        maxIndex = index
print maxNum
print maxIndex'''
print('-' * 20)
print(time.clock() - start)
