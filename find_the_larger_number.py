"""
Problem Statement: Given a number N. Your Mission is to find the largest and the smallest digit of the number.
Note: Print the Largest and Smallest digit
I
Example 1:
Input:
Example 1:
Input:
169
Output:
[9,1]
"""

def find_largest_and_smallest_digit(number):
    # Convert the number to a string
    #"169"
    number_str = str(number)
    
    # Initialize variables to store the largest and smallest digits
    largest_digit = smallest_digit = int(number_str[0])
   
    
    
    # Iterate over each digit in the string representation of the number
    for digit_char in number_str:
        digit = int(digit_char)
        print(digit)
        if digit > largest_digit:
            largest_digit = digit
        if digit < smallest_digit:
            smallest_digit = digit
    
    return [largest_digit, smallest_digit]

# Example usage:
number = 169
result = find_largest_and_smallest_digit(number)
print(result)  # Output: [9, 1]
