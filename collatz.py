import time
start_time = time.time()

def collatz(n):
    collatz_number = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        collatz_number.append(n)
    return collatz_number
    
        
            
len_collatz = []
for n in range(1, 1000000):
    if collatz(n):
        len_collatz.append(len(collatz(n)))


longest_chain = 0
for i in len_collatz:
    if i > longest_chain:
        longest_chain = i

print(len_collatz.index(longest_chain) + 1)
print("process finished --- %s seconds ---" % (time.time() - start_time))
