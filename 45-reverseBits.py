# Day 45 - May 9, 2025
# 190. Reverse Bits
# https://leetcode.com/problems/reverse-bits/

# Solution
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1  # Extract the i-th bit from n
            res = res | (bit << (31 - i))  # Place the bit at the reversed position
        return res