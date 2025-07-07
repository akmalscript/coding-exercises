# Day 75 - July 7, 2025
# 344. Reverse String
# https://leetcode.com/problems/reverse-string/

# Solutions
from typing import List

class Solution:
    # Solution 1 (Two Pointers)
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
       # Time: O(n)  Space: O(1)
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r - 1
    # Solution 2 (Stack)
    def reverseString2(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Time: O(n)  Space: O(n)
        stack = []
        for c in s:
            stack.append(c)

        i = 0
        while stack:
            s[i] = stack.pop()
            i += 1
    # Solution 3 (Recursion)
    def reverseString3(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Time: O(n)  Space: O(n)
        def reverse(l, r):
            if l < r:
                s[l], s[r] = s[r], s[l]
                reverse(l + 1, r - 1)

        reverse(0, len(s) - 1)