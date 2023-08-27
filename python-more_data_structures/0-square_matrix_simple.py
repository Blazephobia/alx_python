def square_matrix_simple(matrix=[]):
    return [[num ** 2 for num in row] for row in matrix]
squared_matrix = square_matrix_simple(original_matrix)
for row in squared_matrix:
    print(row)
