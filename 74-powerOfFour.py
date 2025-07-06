# Day 74 - July 5, 2025
# 342. Power of Four
# https://leetcode.com/problems/power-of-four/

# Solution
from math import log

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and log(n, 4) % 1 == 0