import time
start_time = time.time()

def is_even(n):
     if n % 2 == 0:
          return True
     else:
          return False   

x1 = 1
x2 = 2

sum = 0
while (x1 < 4000000):
     if is_even(x1):
          print(x1)
          sum += x1
     x3 = x1 + x2
     x1 = x2
     x2 = x3 

print("The sum of even numbers are", sum)
print("process finished --- %s seconds ---" % (time.time() - start_time))
     