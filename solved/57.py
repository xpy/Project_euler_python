import time
import helpers

start = time.clock()
k = 0
numerator = 3
denominator = 2
prevNumerator = 1
prevDenominator = 1
results = []
while k < 1000:
    k += 1
    if len(str(numerator)) > len(str(denominator)):
        results.append({'numerator': numerator, 'denominator': denominator})
    tmpNumerator = numerator
    tmpDenominator = denominator
    numerator = numerator * 2 + prevNumerator
    denominator = denominator * 2 + prevDenominator
    prevNumerator = tmpNumerator
    prevDenominator = tmpDenominator

print(len(results))

print('-' * 20)
print(time.clock() - start)
