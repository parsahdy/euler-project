import time
start_time = time.time()

sum_of_squers = []
for i in range(1, 101):
    sum_of_squers.append(i * i)
    result1 = sum(sum_of_squers)

squers_of_sum =[]
for i in range(1, 101):
    squers_of_sum.append(i)
    result2 = sum(squers_of_sum)

print(result2 * result2  - result1)
print("process finished --- %s seconds ---" % (time.time() - start_time))


 