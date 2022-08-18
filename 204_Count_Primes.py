# Time Limit Exceeded
def countPrimes(n):
    prime_numbers = 0

    def is_prime_number(x):
        if x >= 2:
            for y in range(2, x):
                if not (x % y):
                    return False
        else:
            return False
        return True

    for i in range(n):
        if is_prime_number(i):
            prime_numbers += 1
    return prime_numbers

# Another Solution O(n * logn), still time limit exceeded
def countPrimes_2(n):
    if n == 0 or n == 1:
        return 0

    primes = [1] * n
    primes[0] = 0
    primes[1] = 0

    i = 2
    while i < n:
        tmp = i
        if primes[i]:
            tmp += i
            while tmp < n:
                primes[tmp] = 0
                tmp += i
        i += 1

    return sum(primes)

# Solution Accepted
def countPrimes_3(n):
    Primes = [0] * n
    i = 2
    while i * i < n:
        if not Primes[i]:
            j = i
            k = i * j
            while k < n:
                Primes[k] = 1
                j += 1
                k = i * j
        i += 1
    return n - sum(Primes) - 2 if n >= 2 else 0

if __name__ == '__main__':
    print(countPrimes(n = 10))
    print(countPrimes(n = 0))
    print(countPrimes(n = 1))

    print(countPrimes_2(n=10))
    print(countPrimes_2(n=4))
    print(countPrimes_2(n=1))

    print(countPrimes_3(n=10))
    print(countPrimes_3(n=4))
    print(countPrimes_3(n=1))