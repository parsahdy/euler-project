import math
import time
start_time = time.time()

def pathcounter(gridsize):
    p = math.factorial(gridsize * 2) / (math.factorial(gridsize) ** 2)
    return p


print(pathcounter(20))
print("process finished --- %s seconds ---" % (time.time() - start_time))