def divisors(m):
    divisors = []   
    for i in range(1, (m // 2) + 1):
        if m % i == 0:
            divisors.append(i)
    return divisors

abundant_numbers = []
for j in range (1, 100000):
    if sum(divisors(j)) > j:
        abundant_numbers.append(j)

print(abundant_numbers)
