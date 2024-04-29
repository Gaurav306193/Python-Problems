# reverse matrix rowss

def reverse_matrix_rows(matrix):
    print("Original Matrix:")
    for row in matrix:
        print(row)

    reversed_matrix = []
    for row in matrix:
        reversed_matrix.append(list(reversed(row)))

    print("\nMatrix with Reversed Rows:")
    for row in reversed_matrix:
        print(row)

def test():
    N = 4
    M = 4
    Arr = [[0, 1, 1, 1], [0, 1, 0, 1], [0, 0, 0, 0], [1, 1, 1, 1]]
    reverse_matrix_rows(Arr)

test()

