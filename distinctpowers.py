distinct_numbers = []
for a in range(2, 101):
    for b in range(2, 101):
        distinct_numbers.append(a**b)

distinct_numbers = list(set(distinct_numbers))
distinct_numbers_s = sorted(distinct_numbers)
print(len(distinct_numbers_s))


