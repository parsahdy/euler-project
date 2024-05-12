import time
start_time = time.time()

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    return [i for i in range(n + 1) if primes[i]]

primes_between_1_and_10000 = sieve_of_eratosthenes(1000000)
print(len(primes_between_1_and_10000))

print("process finished --- %s seconds ---" % (time.time() - start_time))