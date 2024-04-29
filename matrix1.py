def row_with_max_ones(arr):
    max_ones_row = -1
    max_ones_count = 0
    
    for i, row in enumerate(arr):
        ones_count = sum(row)
        if ones_count > max_ones_count:
            max_ones_count = ones_count
            max_ones_row = i
    
    return max_ones_row

# Function to take user input for a 2D array
def input_array():
    N = int(input("Enter the number of rows: "))
    M = int(input("Enter the number of columns: "))
    arr = []
    for i in range(N):
        row = list(map(int, input(f"Enter space-separated values for row {i+1}: ").split()))
        arr.append(row)
    return arr

# Test the function
def test():
    Arr = input_array()
    max_ones_row = row_with_max_ones(Arr)
    if max_ones_row == -1:
        print("Output: -1")
    else:
        print("Output:", max_ones_row)

# Run the test
test()
