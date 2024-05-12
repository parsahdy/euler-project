matrix = [
    [33, 42, 55, 64],
    [8, 10, 21, 12],
    [23, 14, 15, 16],
    [22, 18, 19, 20]
]

main_diagonal = []
for i in range(len(matrix)):
    main_diagonal.append(matrix[i][len(matrix) - i - 1])


print("Main diagonal of Matrix:", main_diagonal)