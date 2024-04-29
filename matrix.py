"""Problem Statement: Given a 2D array of n x m, consisting of only 1's and O's. 
Your Mission is to find the row Number with consisting the maximum number of 1's.
# notw: Find the 0-based index of the first row that has the maximum number of 1's. 
If grid consist only zeros then return -1.
Example 1:
Input:
Example 1:
N = 4, M = 4
Arr[][] = {{0, 1, 1, 1}, {0, 1, 0, 1), {0, 0, 0, 0}, {1, 1, 1, 1}}
I
Output: 3
"""

def row_with_max_ones(arr):
    max_ones_row = -1
    max_ones_count = 0
    
    for i, row in enumerate(arr):
        ones_count = sum(row)
        if ones_count > max_ones_count:
            max_ones_count = ones_count
            max_ones_row = i
    
    return max_ones_row

# Test the function
def test():
    N = 4
    M = 4
    Arr = [[0, 1, 1, 1], [0, 1, 0, 1], [0, 0, 0, 0], [1, 1, 1, 1]]
    print("Output:", row_with_max_ones(Arr))

# Run the test
test()
