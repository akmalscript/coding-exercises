# Day 65 - June 17, 2025
# 263. Ugly Number
# https://leetcode.com/problems/ugly-number/

# Solution
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        
        for p in [2, 3, 5]:
            while n % p == 0:
                n = n // p
        
        return n == 1