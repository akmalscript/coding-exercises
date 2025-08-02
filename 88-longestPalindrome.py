# Day 88 - August 2, 2025
# 409. Longest Palindrome
# https://leetcode.com/problems/longest-palindrome/

# Solution
class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        res = 0

        for c in s:
            if c in seen:
                seen.remove(c)
                res += 2
            else:
                seen.add(c)

        return res + 1 if seen else res