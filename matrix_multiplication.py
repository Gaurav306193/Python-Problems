# Matrix multiplication

def matrix_multiplication(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print("Invalid dimensions for matrix multiplication!")
        return None

    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

def test():
    N = 4
    M = 4
    Arr = [[0, 1, 1, 1], [0, 1, 0, 1], [0, 0, 0, 0], [1, 1, 1, 1]]

    matrix2 = [[1, 0, 0, 1], [1, 1, 0, 1], [1, 0, 1, 1], [1, 1, 1, 1]]

    result_matrix = matrix_multiplication(Arr, matrix2)

    if Arr:
        print("Matrix1: ")
        for row in Arr:
            print(row)

    if matrix2:
        print("Matrix2 :")
        for row in matrix2:
            print(row)

    if result_matrix:
        print("Result of Matrix Multiplication:")
        for row in result_matrix:
            print(row)

test()
