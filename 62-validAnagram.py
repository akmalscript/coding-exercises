# Day 62 - June 11, 2025
# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/

# Solution
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution 1 (Hash Map)
        return Counter(s) == Counter(t)
    
        # Alternative Solution 1 (Hash Map without 'Counter' built-in function)
        # if len(s) != len(t):
        #     return False

        # countS, countT = {}, {}

        # for i in range(len(s)):
        #     countS[s[i]] = 1 + countS.get(s[i], 0)
        #     countT[t[i]] = 1 + countT.get(t[i], 0)
            
        # for c in countS:
        #     if countS[c] != countT.get(c, 0):
        #         return False

        # return True
    
    def isAnagram2(self, s: str, t: str) -> bool:
        # Solution 2 (Sorting)
        return sorted(s) == sorted(t)