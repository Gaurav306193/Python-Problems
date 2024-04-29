"""Problem Statement: You are playing a game in which you have to find the good number or bad number. 
A number is a good number if the number is divisible by the sum of its digits.
note: Print 'Good Number' if number is a good number else print 'Bad Number'
T
Sample Test 1:
Input:
num = 3
Output: Good Number
Sample Test 2:
Input:
num = 27
Output: Good Number
Sample Test 3 :
input:
num = 16
Output: Bad Number
"""

def is_good_number(num):
    # Calculate the sum of the digits
    digit_sum = sum(int(digit) for digit in str(num))
    #for digit in str(num): This iterates over each character (digit)
    # in the string representation of num. For example, if num is 27,
    # this loop will iterate over the characters '2' and '7'.
    
    # Check if the number is divisible by the sum of its digits
    if num % digit_sum == 0:
        return "Good Number"
    else:
        return "Bad Number"

# Test cases
num1 = 3
num2 = 27
num3 = 16

print("Sample Test 1:")
print("Input:", num1)
print("Output:", is_good_number(num1))  # Output: Good Number

print("Sample Test 2:")
print("Input:", num2)
print("Output:", is_good_number(num2))  # Output: Good Number

print("Sample Test 3:")
print("Input:", num3)
print("Output:", is_good_number(num3))  # Output: Bad Number
