# Day 33 - April 14, 2025
# 136. Single Number
# https://leetcode.com/problems/single-number/

# Solution
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result