"""
1st ques is like they give array in which we have to calculate the sum of array elements which gives the number that is 7
example - array = {1,3, 4, 5, 6}
sum = 7
output = subarray1 = (3,4), subarray2 = {6,1} 
"""

def find_subarrays(arr, target):
    subarrays = []
    current_sum = 0
    left = 0

    for right in range(len(arr)):
        current_sum += arr[right]

        while current_sum > target:
            current_sum -= arr[left]
            left += 1

        if current_sum == target:
            subarrays.append(arr[left:right + 1])

    return subarrays

def pair_subarrays(arr, target):
    subarrays = find_subarrays(arr, target)
    pairs = []
    for subarr in subarrays:
        n = len(subarr)
        for i in range(n):
            for j in range(i+1, n):
                pairs.append([subarr[i], subarr[j]])
    return pairs

# Test cases
arr1 = [1, 3, 4, 5, 6]
target1 = 7
print("Test Case 1:")
print(pair_subarrays(arr1, target1))

arr2 = [2, 4, 6, 3, 7, 8, 3]
target2 = 10
print("\nTest Case 2:")
print(pair_subarrays(arr2, target2))

arr3 = [1, 2, 3, 4, 5]
target3 = 9
print("\nTest Case 3:")
print(pair_subarrays(arr3, target3))



"""

arr2 = [2, 4, 6, 3, 7, 8, 3]
target2 = 10
print("\nTest Case 2:")
print(find_subarrays(arr2, target2))

arr3 = [1, 2, 3, 4, 5]
target3 = 9
print("\nTest Case 3:")
print(find_subarrays(arr3, target3))

"""