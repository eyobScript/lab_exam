def find_matrix_shape(matrix):
    Rows = len(matrix)
    Cols = len(matrix[0]) if matrix else 0
    return (Rows, Cols)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(find_matrix_shape(matrix))