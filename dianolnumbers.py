import numpy as np

def matrix_generator(n):
    matrix = np.zeros((n, n), dtype='int32')

    x, y = n//2, n//2
    num = 1
    dx, dy = 0, 1
    steps = 1

    while num <= n*n:
        for _ in range(2):
            for _ in range(steps):
                if 0 <= x < n and 0 <= y < n:
                    matrix[x][y] = num
                    num += 1
                x += dx
                y += dy
            
            dx, dy = dy, -dx
        steps += 1

    return matrix

spiral_matrix = matrix_generator(1001)

n = len(spiral_matrix)
main_diameter = [spiral_matrix[i][i] for i in range(n)]
minor_diameter = [spiral_matrix[i][n - i - 1] for i in range(n)]

merged_list = []
for i in main_diameter + minor_diameter:
    if i not in merged_list:
        merged_list.append(i)

print(sum(merged_list))
