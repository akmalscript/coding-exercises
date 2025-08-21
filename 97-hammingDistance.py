# Day 97 - August 20, 2025
# 461. Hamming Distance
# https://leetcode.com/problems/hamming-distance/

# Solution
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        count = 0
        while xor:
            xor &= xor - 1  # removes the lowest set bit
            count += 1
        return count