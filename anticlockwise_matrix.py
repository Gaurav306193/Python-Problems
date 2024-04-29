# 2nd question is like we have to rotate a matrix anticlockwise and print the result matrix
# do not take user input

def rotate_anticlockwise(matrix):
    # Transpose the matrix
    transposed_matrix = [list(row) for row in zip(*matrix)]
    #(*matrix)= trandpose of matrix    
    # Reverse each row to get the anticlockwise rotation
    rotated_matrix = [list(reversed(row)) for row in transposed_matrix]
    
    return rotated_matrix

# Test case
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotated_matrix = rotate_anticlockwise(matrix)

# Print the rotated matrix
for row in rotated_matrix:
    print(row)


