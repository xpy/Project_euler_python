import time
import helpers

start = time.clock()
lychrels =[]

for num in range(10000):
    k=50
    flag = True
    next = num
    while(k>0):
        next = next+int(str(next)[::-1])
        strNext = str(next)
        if(strNext == strNext[::-1]):break
        k-=1
    else:
        lychrels.append(num)

print(len(lychrels))
print '-' * 20
print time.clock() - start