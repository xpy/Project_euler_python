import time
import helpers

# 8581146 255
# 145
# 56
start = time.clock()
numsThat = {1: {1},89: {89}}
squares = {}
for i in range(0,10):
    squares[str(i)] = i*i
def square_digit_chains(starting_number,queue):
    '''
    @param starting_number:
    @param queue:
    @type queue: set
    @return:
    '''
    for i in numsThat:
        if starting_number in numsThat[i]:
            numSum = i
            break
    else:
        if starting_number < 1000:
            queue.add(starting_number)
        numSum = sum([squares[i] for i in str(starting_number)])
        return square_digit_chains(numSum,queue)
    numsThat[numSum] |= queue
    queue.clear()
    return numSum

numOf89s = 0
for i in range(1,10000000):
    if square_digit_chains(i,set()) == 89:
        numOf89s+=1
    if(not i%100000):print i;
print numOf89s
print time.clock() - start