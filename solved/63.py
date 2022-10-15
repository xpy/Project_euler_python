import time
import helpers

start = time.perf_counter()

power = 1
index = 1
num = index ** power
nums = []
while len(str(num)) == power:
    while len(str(num)) == power:
        print(len(str(num)), num, power)
        nums.append(num)
        power += 1
        num = index ** power
    index += 1
    power = 1
    num = index ** power

print(len(nums))
print('-' * 20)
print(time.perf_counter() - start)
