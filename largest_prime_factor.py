"""
    Largest prime factor
    Problem 3
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
"""


def is_prime(n):
    for i in range(2, int(n ** .5 + 1)):
        if n % i == 0:
            return False
    return True

def is_prime(n):
    if n % 2 == 0: return False
    for i in xrange(3, int(n**0.5) + 1, 2):
        if n % i == 0: return False
    return True


def fibonacci(n):
    a, b = 0, 1
    for i in range(0, n):
        yield a
        a, b = b, a + b


def prime_numbers():
    x = 1
    while True:
        is_prime = True
        for n in xrange(1, int(x / 2) + 1):
            if n != 1 and x % n == 0:
                is_prime = False
        if is_prime:
            yield x
        x = x + 1


def find_largest_prime_factor(primes, number):
    x = 0
    for n in primes:
        if n >= number / 2:
            break
        if number % n == 0:
            yield n
            x = n


n = 600851475143
i = 2
while i * i < n:
    while n % i == 0:
        n = n / i
    i = i + 1
print n
