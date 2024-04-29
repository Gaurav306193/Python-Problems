#Write a program to calculate the pairs count in the given array such that the sum of the pairs is divisible by 2.

#Input: A[] = {2,2,1, 7, 5, 3), (check 2 s divisible hai ya nii)
#Output: 7
#pair -> (2,2), (1,7), (1,5), (1,3), (7,5), (7,3), (5,3)        write the code in python and do not allow duplicate pair 

def count_pairs(arr):
    pair_set = set()
    n = len(arr)
    pair_count = 0
    for i in range(n):
        for j in range(i+1, n):
            # Check if the pair is not already encountered
            if (arr[i], arr[j]) not in pair_set and (arr[j], arr[i]) not in pair_set:
                if (arr[i] + arr[j]) % 2 == 0:
                    pair_count += 1
                    pair_set.add((arr[i], arr[j]))
    return pair_count

# Test the function
A = [2, 2, 1, 7, 5, 3, 2, 2]
print("Output:", count_pairs(A))


