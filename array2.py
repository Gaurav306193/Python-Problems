"""
Problem Statement: Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.
The union of two arrays can be defined as the common and distinct elements in the two arrays.
note: Elements in the union should be in ascending order.
Example 1:
Input: n 5, m = 3
arr1= [1, 2, 3, 4, 6]
arr2 = [2, 3, 5]
Output: [1, 2, 3, 4, 5, 6] I
*/
"""
def find_union(arr1, arr2):
    n = len(arr1) # [1,2,3,4,6]
    m = len(arr2) # [2,3,5]
    i = 0  # Pointer for arr1
    j = 0  # Pointer for arr2
    union = []

    while i < n and j < m: # 2<5 and 0<3
        if arr1[i] < arr2[j]: # 3<5-- True
            union.append(arr1[i]) #[1,2,3,4]
            i += 1  # 3
        elif arr1[i] > arr2[j]:
            union.append(arr2[j])
            j += 1
        else:  # If arr1[i] == arr2[j]
            union.append(arr1[i])
            i += 1
            j += 1

    # Add remaining elements from arr1
    while i < n:
        union.append(arr1[i])
        i += 1

    # Add remaining elements from arr2
    while j < m:
        union.append(arr2[j])
        j += 1

    return union

# Example usage:
arr1 = [1, 2, 3, 4, 6]
arr2 = [2, 3, 5]
result = find_union(arr1, arr2)
print("Output:", result)  # Output: [1, 2, 3, 4, 5, 6]

    