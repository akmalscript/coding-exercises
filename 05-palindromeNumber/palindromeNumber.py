# Day 5 - February 18, 2025
# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/

# Solution
def palindromeNumber(x):
    # Negative numbers cannot be palindromes
    if x < 0:
        return False
    
    # Store the original value
    original = x
    reversed_number = 0

    # Reverse the number
    while x > 0:
        last_digit = x % 10  # Get the last digit
        reversed_number = reversed_number * 10 + last_digit  # Append the last digit to the reversed number
        x = x // 10  # Remove the last digit from x
    
     # Check if the reversed number is the same as the original number
    return reversed_number == original

print(palindromeNumber(121))  # Output: True
print(palindromeNumber(-121)) # Output: False
print(palindromeNumber(10))   # Output: False