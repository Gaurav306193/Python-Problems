"""
Problem Statement: Given two strings S1 and S2 of lowercase alphabets, find the list of uncommon characters for the two strings.
A character is uncommon if it is present only in one of the strings. it is either present in S1 or S2, but not in both.
Note :
1. Both the strings contain only lowercase alphabets and can contain duplicates.
I 2. Return the uncommon characters in sorted order and can not contain duplicates.
Example 1:
s1 digital, s2 = ninja
Output: dgjlnt
"""
def find_uncommon_characters(s1, s2):
    # Convert strings to sets to remove duplicates
    set_s1 = set(s1)
    set_s2 = set(s2)
    
    # Find the symmetric difference between the sets
    uncommon_chars = set_s1.symmetric_difference(set_s2)
    
    # Convert the symmetric difference set to a sorted list
    uncommon_chars_sorted = sorted(uncommon_chars)
    
    return uncommon_chars_sorted

# Example usage:
s1 = "digital"
s2 = "ninja"
result = find_uncommon_characters(s1, s2)
print(''.join(result))  # Output: dgjlnt
