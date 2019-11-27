def is_palindromic2(num):
    num = str(num)
    l = len(num) - 1
    for index, i in enumerate(num):
        if num[l - index] != i:
            return False
    return True


def is_palindromic(num):
    return


def shieve_primes_to(to):
    prime_set = [True for i in range(0, to)]
    i = 2
    while i < to:
        for j in range(i * 2, to, i):
            prime_set[j] = False
        i += 1
        while i < len(prime_set) and not prime_set[i]:
            i += 1

    return [index for index, i in enumerate(prime_set) if i][2:]


def primes_to(to):
    odds = [2]
    flag = True
    prek = 0
    for cur in range(3, to, 2):
        if flag:
            sqrt_cur = cur ** .5
            # if sqrt_cur == int(sqrt_cur):
            #     flag = False
            while odds[prek] < sqrt_cur:
                prek += 1
        else:
            flag = True
        if flag:
            for i in range(0, prek + 1):
                if not cur % odds[i]:
                    flag = False
                    break
            else:
                odds.append(cur)
    return odds


def is_permutation(str1, str2):
    str1 = list(str(str1))
    str2 = list(str(str2))
    str1.sort()
    str2.sort()
    return str1 == str2


def triangle(n):
    return int(n * (n + 1) / 2)


def square(n):
    return int(n ** 2)


def pentagonal(n):
    return int(n * (3 * n - 1) / 2)


def generalized_pentagonal2(n):
    # n += 1
    sign = -1 if n % 2 else 1
    n = n // 2 * sign
    return int(n * (3 * n - 1) / 2)


PENDS = {}


def generalized_pentagonal(n, sign):
    # n += 1
    n = n * sign
    if PENDS.get(n, None) is not None:
        return PENDS.get(n)
    PENDS[n] = int(n * (3 * n - 1) / 2)
    return PENDS[n]


def hexagonal(n):
    return int(n * (2 * n - 1))


def heptagonal(n):
    return int(n * (5 * n - 3) / 2)


def octagonal(n):
    return int(n * (3 * n - 2))


def is_pentagonal(num):
    # delta = 1 + 24 * num
    # x1 = (1 + delta**.5) / 6
    x = (1 + (1 + 24 * num) ** .5) / 6
    # if x == int(x):
    #     print x , int(x),x == int(x)
    return x.is_integer()


primes = []


def roots_2(a, b, c):
    return abs(-b + (b ** 2 - 4 * a * c) ** .5) / (2 * a)


def is_prime(num):
    global primes
    if num in primes:
        return True
    if num == 2:
        return True
    sqrt = num ** .5
    int_sqrt = int(sqrt)
    if sqrt == int_sqrt:
        return False
    for i in range(3, int_sqrt + 1, 2):
        if num % i == 0:
            return False
    if not (num % 2 == 0):
        primes.append(num)
        return True


class Primes:
    primes = []
    prime_set = set()

    def __init__(self, to) -> None:
        self.to = to
        self.current = 1
        super().__init__()

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.to:
            raise StopIteration
        else:
            self.current += 1
            while not is_prime(self.current):
                self.current += 1
                if self.current > self.to:
                    raise StopIteration

            self.primes.append(self.current)
            self.prime_set.add(self.current)
            return self.current

    def _is_prime(self, num):
        for p in self.primes:
            if num % p == 0:
                return False
            if p ** 2 > num:
                return True
        return True


def are_relative_prime(a, b):
    min_num = min(a, b)
    max_num = max(a, b)
    while min_num > 1:
        tmp = min_num
        min_num = max_num % min_num
        max_num = tmp
    return min_num == 1


def phi(num):
    # print [i for i in range(2,num) if areRelativePrime(num , i)]
    # if (isPrime(num
    #     return num - 1
    phi_num = 0
    phi_cache = []
    for i in range(2, num):
        for j in phi_cache:
            if i % j == 0:
                break
        else:
            if are_relative_prime(num, i):
                phi_num += 1
            else:
                phi_cache.append(i)
    return phi_num + 1
    # return len([i for i in range(2,num) if areRelativePrime(num , i)])+1


def is_bouncy(num):
    num2 = list(str(num))
    ordered_num = sorted(num2)
    return not (num2 == ordered_num or num2 == ordered_num[::-1])


_check_point_ = 0


def check_point(num):
    global _check_point_
    if _check_point_ % num == 0:
        print(_check_point_)
    _check_point_ += 1


def fraction(num):
    truples = set()
    sequence = []

    def fraction_internal(num, a=None, m=0, d=1):
        a = a if a else int(num ** .5)
        truple = (a, m, d)
        next_m = d * a - m
        next_d = int((num - next_m ** 2) / d)
        next_a = int((int(num ** .5) + next_m) / next_d)
        if truple in truples:
            return sequence
        truples.add(truple)
        sequence.append(a)
        return fraction_internal(num, next_a, next_m, next_d)

    return fraction_internal(num)


def convergents(num):
    fraction_seq = fraction(num)
    convergent_list = []
    convergent_list.append((fraction_seq[0], 1))
    convergent_list.append((fraction_seq[1] * convergent_list[-1][0] + 1, fraction_seq[1]))
    for i in fraction_seq[2:]:
        a = (i * convergent_list[-1][0] + convergent_list[-2][0], i * convergent_list[-1][1] + convergent_list[-2][1])
        convergent_list.append(a)

    for i in fraction_seq[1:]:
        a = (i * convergent_list[-1][0] + convergent_list[-2][0], i * convergent_list[-1][1] + convergent_list[-2][1])
        convergent_list.append(a)
    return convergent_list


def get_divisors(num, start=2, step=1):
    i = start
    res = [1, num]
    limit = num // start
    while i <= limit:
        if num % i == 0:
            limit = num // i
            res += [i, limit]
        i += step
    return sorted(set(res))
