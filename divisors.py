def divisors(n):
    divisors = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors
        

amicable = []
for i in range(2, 10001):
    sum_div_i = sum(divisors(i))
    if sum_div_i < 10000 and sum_div_i != i:
        sum_div_sum = sum(divisors(sum_div_i))
        if sum_div_sum == i:
            amicable.append(i)

print(amicable)
print(sum(amicable))



