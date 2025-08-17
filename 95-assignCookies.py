# Day 95 - August 16, 2025
# 455. Assign Cookies
# https://leetcode.com/problems/assign-cookies/

# Solution
from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        i = j = 0
        while i < len(g):
            while j < len(s) and g[i] > s[j]:
                j += 1
            if j == len(s):
                break
            i += 1
            j += 1
        return i