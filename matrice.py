# Input dimensions for the first matrix
rows1 = int(input("Enter number of rows for the first matrix: "))
cols1 = int(input("Enter number of columns for the first matrix: "))

# Input dimensions for the second matrix
rows2 = int(input("Enter number of rows for the second matrix: "))
cols2 = int(input("Enter number of columns for the second matrix: "))

# Initialize matrices with zeroes
matrix1 = [[0] * cols1 for _ in range(rows1)]
matrix2 = [[0] * cols2 for _ in range(rows2)]

# Get values for the first matrix
print("Enter values for the first matrix:")
for i in range(rows1):
    row_values = input(f"Enter values for row {i + 1} (space-separated): ").split()
    for j in range(cols1):
        matrix1[i][j] = int(row_values[j])

# Get values for the second matrix
print("Enter values for the second matrix:")
for i in range(rows2):
    row_values = input(f"Enter values for row {i + 1} (space-separated): ").split()
    for j in range(cols2):
        matrix2[i][j] = int(row_values[j])

# Display Matrix 1
print("\nMatrix 1:")
for i in range(rows1):
    for j in range(cols1):
        print(matrix1[i][j], end=' ')
    print()

# Display Matrix 2
print("\nMatrix 2:")
for i in range(rows2):
    for j in range(cols2):
        print(matrix2[i][j], end=' ')
    print()

# Matrix Addition
if rows1 == rows2 and cols1 == cols2:
    print("\nSum of Matrix 1 and Matrix 2:")
    for i in range(rows1):
        for j in range(cols1):
            print(matrix1[i][j] + matrix2[i][j], end=' ')
        print()
else:
    print("\nMatrix addition is not possible. The matrices must have the same dimensions.")

# Matrix Multiplication
if cols1 == rows2:
    # Initialize the product matrix with zeroes
    product_matrix = [[0] * cols2 for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            sum_product = 0
            for k in range(cols1):
                sum_product += matrix1[i][k] * matrix2[k][j]
            product_matrix[i][j] = sum_product

    print("\nProduct of Matrix 1 and Matrix 2:")
    for i in range(rows1):
        for j in range(cols2):
            print(product_matrix[i][j], end=' ')
        print()
else:
    print("\nMatrix multiplication is not possible. The number of columns in Matrix 1 must be equal to the number of rows in Matrix 2.")

# Matrix Transpose
# Transpose of Matrix 1
transpose_matrix1 = [[0] * rows1 for _ in range(cols1)]
for i in range(rows1):
    for j in range(cols1):
        transpose_matrix1[j][i] = matrix1[i][j]

# Transpose of Matrix 2
transpose_matrix2 = [[0] * rows2 for _ in range(cols2)]
for i in range(rows2):
    for j in range(cols2):
        transpose_matrix2[j][i] = matrix2[i][j]

print("\nTranspose of Matrix 1:")
for i in range(cols1):
    for j in range(rows1):
        print(transpose_matrix1[i][j], end=' ')
    print()

print("\nTranspose of Matrix 2:")
for i in range(cols2):
    for j in range(rows2):
        print(transpose_matrix2[i][j], end=' ')
    print()
