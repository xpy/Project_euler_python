import time

# inputFile = open('resources/', 'r')

start_time = time.clock()

maxpal = 0
for i in range(100, 1000):
    for f in range(i, 1000):
        num = i * f
        strnum = str(num)
        if strnum == strnum[::-1]:
            maxpal = max(num, maxpal)

print("\033[0;35mpals", maxpal, "\033[0m")
print(time.clock() - start_time)
