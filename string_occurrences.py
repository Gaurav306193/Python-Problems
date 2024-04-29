"""
Problem Statement: You have given two stirng s1 and s2,
your mission is to calculate the sum of the character occurrences of the s2 string in string s1.
Example 1:
Input:
s1 = "helloworld" sum = 1 + 2 = 3
s2 = "do"
Output: 3
Example 2:
Input:
s1 = "developer" sum = 1)
s2 = "dev"
Output: 5 in python

"""

def sum_of_occurrences(s1, s2):
    count = 0 
    # here count is variable
    for char in s2:
        
        count += s1.count(char) #here count is function
        # count() is a occurrences of substring
    return count

# Example usage:
s1 = "helloworld"
s2 = "do"
result = sum_of_occurrences(s1, s2)
print("Output:", result)  # Output: 3

s1 = "developer"
s2 = "dev"
result = sum_of_occurrences(s1, s2)
print("Output:", result)  # Output: 5
