# Day 59 - June 5, 2025
# 231. Power of Two
# https://leetcode.com/problems/power-of-two/

# Solution
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0