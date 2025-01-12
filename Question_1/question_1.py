def find_matrix_shape(matrix):
    Rows = len(matrix)
    Cols = len(matrix[0]) if matrix else 0
    return (Rows, Cols)
