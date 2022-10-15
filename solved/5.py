import time

# inputFile = open('resources/', 'r')

start_time = time.perf_counter()

nums = [11, 12, 13, 14, 15, 16, 17, 18, 19][::-1]

i = 1
while True:
    num = i * 20
    for k in nums:
        if num % k:
            break
    else:
        print("\033[0;35mnum", num, "\033[0m")
        break
    i += 1

print(time.perf_counter() - start_time)
