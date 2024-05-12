import time
start_time = time.time()

def is_prime(n):
    prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prime = False
            break
    return prime
    
prime_number = []    
for i in range(2, 1000000):
    if is_prime(i):
        prime_number.append(i)

print(prime_number[10000])
print("process finished --- %s seconds ---" % (time.time() - start_time))

