def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for num in row:
            # Use str.format() to format and print each integer
            print("{:d}".format(num), end=" ")
        print()  # Move to the next line after printing a row

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
