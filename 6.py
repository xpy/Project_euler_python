import time

# inputFile = open('resources/', 'r')

start_time = time.clock()

psum = 0
ssum = 0
for i in range(1, 101):
    ssum += i ** 2
    psum += i

print("\033[0;35mssum-", psum**2 - ssum, "\033[0m")
print(time.clock() - start_time)
