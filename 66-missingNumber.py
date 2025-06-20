# Day 66 - June 19, 2025
# 268. Missing Number
# https://leetcode.com/problems/missing-number/

# Solution
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2
        return total - sum(nums)