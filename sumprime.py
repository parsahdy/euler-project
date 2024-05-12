def is_prime(n):
    prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prime = False
            break
    return prime

sum_prime = []
for i in range(2, 2000000):
    if is_prime(i):
        sum_prime.append(i)


print(sum(sum_prime))