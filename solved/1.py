import time

# inputFile = open('resources/', 'r')

start_time = time.clock()

a = sum(i for i in range(0, 1000) if i % 5 == 0 or i % 3 == 0)
print(a)

print(time.clock() - start_time)
