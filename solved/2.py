import time

# inputFile = open('resources/', 'r')

start_time = time.clock()

fib = [1, 2]
evens = 0
while fib[1] < 4 * (10 ** 6):
    if fib[1] % 2 == 0:
        evens += fib[1]
    fib[0], fib[1] = fib[1], fib[0] + fib[1]
s = evens
print("\033[0;35m", s, "\033[0m")
print(time.clock() - start_time)
