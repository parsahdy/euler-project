def proper_divisors_sum(n):
    divisors_sum = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum

abundant_numbers = []
for num in range(12, 28123):
    if proper_divisors_sum(num) > num:
        abundant_numbers.append(num)

abundant_sums = set()
for i in range(len(abundant_numbers)):
    for j in range(i, len(abundant_numbers)):
        abundant_sums.add(abundant_numbers[i] + abundant_numbers[j])

non_abundant_sums = set(range(1, 28123)) - abundant_sums

result = sum(non_abundant_sums)
print(result)





