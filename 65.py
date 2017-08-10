import time
import helpers
import math

# inputFile = open('resources/', 'r')

start = time.clock()

target = 100
skata = [x for sub in [[1, i * 2, 1] for i in range(1, math.ceil(target / 3) + 1)] for x in sub]
print('skata',skata)
# -1 because of the step we add in the end and -1 for the 0 key
target2 = target - 2
numerator = skata[target2]
denominator = 1
for next_numerator in reversed(skata[0:target2]):
    d2 = denominator
    denominator = numerator
    numerator = next_numerator * numerator + d2

print("========================")
print(denominator + 2 * numerator, numerator)
print('?????')
print(sum([int(i) for i in (str(denominator + 2 * numerator))]))
print(skata)

print(time.clock() - start)
