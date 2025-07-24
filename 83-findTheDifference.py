# Day 83 - July 23, 2025
# 389. Find the Difference
# https://leetcode.com/problems/find-the-difference/

# Solutions
from collections import Counter

class Solution:
    # Solution 1 : Bit Manipulation
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        for c in s:
            res = res ^ ord(c)
        for c in t:
            res = res ^ ord(c)

        return chr(res)

    # Solution 2 : ASCII
    def findTheDifference2(self, s: str, t: str) -> str:
        sum_s, sum_t = 0, 0
        for c in s:
            sum_s += ord(c)
        for c in t:
            sum_t += ord(c)
        return chr(sum_t - sum_s)

    # Solution 3 : Hashmap
    def findTheDifference3(self, s: str, t: str) -> str:
        count_s, count_t = Counter(s), Counter(t)

        for c in count_t:
            if c not in count_s:
                return c
            if count_s[c] < count_t[c]:
                return c