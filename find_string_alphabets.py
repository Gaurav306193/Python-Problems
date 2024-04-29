"""
/*
Problem Statement: You have given a stirng s and a character ch, your task is to find the first and last occurrence of the given charater.
note: Return the first and last occurrence indexes
Example 1:
I
Input:
Input:
s = "developer"
ch = "e"
Output: {1,7}
"""

def find_first_and_last_occurrence(s, ch):
    first_occurrence = s.find(ch)
    last_occurrence = s.rfind(ch)
    return [first_occurrence, last_occurrence]

# Example usage:
s = "developer"
ch = "r"
result = find_first_and_last_occurrence(s, ch)
print(result)  # Output: [1, 7]


def find_first_and_last_occurrence_with_alphabets(s, ch):
    first_occurrence = s.find(ch)
    last_occurrence = s.rfind(ch)
    occurred_alphabets = {}
    for i in range(len(s)):
        if s[i] == ch:
            occurred_alphabets[s[i]] = [first_occurrence, last_occurrence]
    return occurred_alphabets

# Example usage:
s = "developer"
ch = "r"
result = find_first_and_last_occurrence_with_alphabets(s, ch)
print(result)  # Output: {'e': [1, 7]}
