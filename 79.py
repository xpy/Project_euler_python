import time
import helpers

start = time.clock()

file = open('resources/keylog.txt', 'r')
numbers = {}
for i in range(0, 10):
    numbers[str(i)] = {'before': [], 'after': []}
for i in [str(int(i)) for i in file.readlines()]:
    for index, j in enumerate(i):
        if index == 0:
            if i[1] not in numbers[j]['after']:
                numbers[j]['after'].append(i[1])
            if i[2] not in numbers[j]['after']:
                numbers[j]['after'].append(i[2])
        elif index == 1:
            if i[0] not in numbers[j]['before']:
                numbers[j]['before'].append(i[0])
            if i[2] not in numbers[j]['after']:
                numbers[j]['after'].append(i[2])
        else:
            if i[0] not in numbers[j]['before']:
                numbers[j]['before'].append(i[0])
            if i[1] not in numbers[j]['before']:
                numbers[j]['before'].append(i[1])

numbers2 = {}
for i in [i for i in numbers if len(numbers[i]['before']) or len(numbers[i]['after'])]:
    numbers[i]['after'].sort()
    numbers[i]['before'].sort()
    numbers2[i] = numbers[i]
    print(i, numbers[i])

startResults = []
endResults = []
while len(numbers2):
    for i in numbers2:
        num = numbers2[i]
        if len(num['after']) == 0:
            endResults.insert(0, i)
            numbers2.pop(i)
            for j in numbers2:
                for index, k in enumerate(numbers2[j]['after']):
                    if k == i:
                        numbers2[j]['after'].pop(int(index))
            break
        if len(num['before']) == 0:
            startResults.insert(0, i)
            numbers2.pop(i)
            for j in numbers2:
                for index, k in enumerate(numbers2[j]['before']):
                    if k == i:
                        numbers2[j]['before'].pop(int(index))
            break

# for i in [ i for i in numbers2 if len(numbers2[i]['before']) or len(numbers2[i]['after'])]:
#     print i,numbers2[i]
# 73162890
print(str.join('', startResults[::-1]) + str.join('', endResults))

print('-' * 20)
print(time.clock() - start)
