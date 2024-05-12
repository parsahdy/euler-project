import time
start_time = time.time()

def is_multiple(n):
    for i in range(1, 21):
        if n % i != 0:
            return False
    return True
        
    

smallest_number = 0
for number in range(1, 1000000000):
    if is_multiple(number):
        smallest_number += number
        break

print(smallest_number)
print("process finished --- %s seconds ---" % (time.time() - start_time))
