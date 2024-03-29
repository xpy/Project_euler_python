import time
import helpers

start = time.perf_counter()


# print 0b100 & 0b110
# helpers.primesTo(1000000)


def make_thing(prime, num):
    sumz = 0
    target = 8
    for i in range(0, 10):
        # print(prime.replace(num, str(i)))
        sumz += 1 if (not (prime[0] == num and i == 0)) and (int(prime.replace(num, str(i)))in primes_set) else 0
        if (sumz + 10 - i) < target:
            return False
        # print(sumz)
    return sumz == target


def asdf(prime):
    str_prime = str(prime)
    checked_str = []
    for num in str_prime:
        if num in checked_str or num == str_prime[-1]:
            continue
        checked_str.append(num)
        if make_thing(str_prime, num):
            return True
    return False


# print(make_thing("28229", "2"))
# print(make_thing("121313", "1"))

cnt = 0
primes = helpers.shieve_primes_to(1000000)
primes_set = set(primes)
for aprime in primes:
    if asdf(aprime):
        print("---------------" + str(aprime))
        break

# print([prime for prime in helpers.primesTo(1000000) if prime > 100000])
print('-' * 20)
print(time.perf_counter() - start)
