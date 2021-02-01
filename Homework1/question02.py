# Question 2 (10%)

# Write a function called 'primes'
#
# primes should either take no arguments (i.e. primes()),
# in which case it returns the first 10 prime numbers
# or it should take one argument, n (e.g. primes(16)) in which
# case it should return the first n prime numbers (e.g. the
# first 16 primes, in the previous example.)
import sys


def is_prime(number):
    result = True;
    for i in range(2, number):
        if number % i == 0:  # has a division, not prime
            result = False
            break
    return result


def primes(n=10):
    numbers = []

    if n < 1:
        return numbers

    for i in range(2, sys.maxsize):
        if is_prime(i):
            numbers.append(i)
            if len(numbers) == n:
                break
    return numbers


print(primes())
print(primes(1))
print(primes(16))
print(primes(0))

# Examples:
# primes() should return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# primes(1) should return [2]
# primes(16) should return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
# primes(0) should return []


