def triangle_numbers(limit):
    triangle_numbers = []
    for n in range(1, limit + 1):
        triangle_number = (n * (n + 1)) // 2
        triangle_numbers.append(triangle_number)
    return triangle_numbers


def factors(m):
    factor_count = 0
    for j in range(1, int(m ** 0.5) + 1):
        if m % j == 0:
            factor_count += 2
    return factor_count


first_triangle = 0
limit = 100000
for i in triangle_numbers(limit):
    if factors(i) > 500:
        first_triangle += i
        break
        
print(first_triangle)
     
        


