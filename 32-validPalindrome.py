# Day 32 - April 12, 2025
# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/

# Solution
class Solution:
    # Solution 1
    def isPalindrome(self, s: str) -> bool:
        # Filter the string to only alphanumeric characters and convert to lowercase
        filtered = ''.join(char.lower() for char in s if char.isalnum())
        # Check if the filtered string is the same forwards and backwards
        return filtered == filtered[::-1]

    # Solution 2 (Two Pointers)
    def isPalindrome2(self, s: str) -> bool:
        # Start with two pointers: one at the beginning, one at the end
        l, r = 0, len(s) - 1

        # Keep checking characters while left is less than right
        while l < r:
            # Move the left pointer if the character is not alphanumeric
            while l < r and not self.alphaNum(s[l]):
                l += 1
            # Move the right pointer if the character is not alphanumeric
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            # Compare the characters (converted to lowercase)
            if s[l].lower() != s[r].lower():
                return False  # Not a palindrome
            # Move both pointers inward
            l += 1
            r -= 1

        # If all characters matched, it's a palindrome
        return True

    def alphaNum(self, c: str) -> bool:
        # Check if character is a letter (A-Z or a-z) or number (0-9)
        return (
            ('A' <= c <= 'Z') or
            ('a' <= c <= 'z') or
            ('0' <= c <= '9')
        )