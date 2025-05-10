# Day 46 - May 10, 2025
# 191. Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/

# Solution
class Solution:
    # Solution 1 (Basic Bitwise Method)
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1  # add 1 if the last bit is 1
            n >>= 1         # shift bits to the right
        return count
    
    # Solution 2 (Brian Kernighan's algorithm)
    def hammingWeight2(self, n: int) -> int:
        count = 0
        while n:
            n &= (n - 1)  # remove the rightmost set bit
            count += 1
        return count