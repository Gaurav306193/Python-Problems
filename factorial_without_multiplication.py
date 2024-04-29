# find the factorial without using *

def findFactorial(n):
    ans = n
    for i in range(n - 1, 0, -1):
        sum = 0
        for j in range(i):
            sum += ans
        ans = sum
    return ans

# Test the function
print(findFactorial(5))  # Output should be 120
