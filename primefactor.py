def is_prime(n):
    prime = True
    for i in range(2, int((n ** 0.5) + 1)):
        if n % i == 0:
            prime = False
            break
        return prime
    


def factor(m):
    for i in range(1, m):
        if is_prime(i) and m % i == 0:
                m = m / i
                print(i)
  

print(factor(600851475143))
