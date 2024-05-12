import time
start_time = time.time()

def is_prime(n):
    prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            prime = False
            break
    return prime

prime_count = 0
last_prime_number = 0

for i in range(2, 1001):
    if is_prime(i):
        last_prime_number = i
        prime_count += 1

print("We had", prime_count, "prime Numbers")
print("Last prime nuber is", last_prime_number)
print("process finished --- %s seconds ---" % (time.time() - start_time))

