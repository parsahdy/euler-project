import time
start_time = time.time()

def Pythagorean(a, b, c):
    if a < b < c and ((a ** 2 + b ** 2) == c ** 2):
        return True
    return False
    

for a in range(1, 1000):
    for b in range(1, 1000):
        for c in range(1, 1000):
            if Pythagorean(a, b, c) and a + b + c == 1000:
                print(a)
                print(b)
                print(c)
                print(a * b * c)

print("process finished --- %s seconds ---" % (time.time() - start_time))

