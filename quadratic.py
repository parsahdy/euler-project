import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def count_consecutive_primes(a, b):
    n = 0
    while True:
        value = n**2 + a*n + b
        if not is_prime(value):
            break
        n += 1
    return n

max_primes = 0
product_coefficients = 0

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        primes_count = count_consecutive_primes(a, b)
        if primes_count > max_primes:
            max_primes = primes_count
            product_coefficients = a*b

print(f"The product of coefficients is: {product_coefficients}")
