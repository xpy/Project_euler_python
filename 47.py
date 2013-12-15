import time
import helpers

start = time.clock()

primesList = helpers.primesTo(1000)
primeListLength  =   len(primesList)
print 'Started!'

def getDistinctPrimeFactors(num,res):
    startIndex =primeListLength
    halfNum = int(num/2)+1
    if(halfNum<primesList[primeListLength-1]):
        for index,prime in enumerate(primesList):
            if(prime>=halfNum):
                startIndex = index+1
                break
    for prime in [prime for prime in primesList[startIndex::-1] if not num%prime]:
        if prime not in res:
            res.append(prime)
        res = getDistinctPrimeFactors(num/prime,res)
        break
    return res

k=0
numOfDistinct = 4
count = 0
while(count<numOfDistinct and k <200000):
    k+=1
    if len(getDistinctPrimeFactors(k,[]) )== numOfDistinct:
        count+=1
    else:
        count = 0
else:
    print k-numOfDistinct+1

print '-' * 20
print time.clock() - start