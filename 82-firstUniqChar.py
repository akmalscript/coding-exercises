# Day 82 - July 21, 2025
# 387. First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/

# Solution
from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Create a dictionary to count the frequency of each character
        count = defaultdict(int)  # Default value for int is 0

        # First pass: count each character's frequency
        for c in s:
            count[c] += 1

        # Second pass: find the first character with a count of 1
        for i, c in enumerate(s):
            if count[c] == 1:
                return i  # Return the index of the first unique character

        # If no unique character is found, return -1
        return -1