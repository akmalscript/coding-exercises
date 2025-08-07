# Day 90 - August 6, 2025
# 414. Third Maximum Number
# https://leetcode.com/problems/third-maximum-number/

# Solution
from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float('-inf')
        
        for num in nums:
            if num in (first, second, third):
                continue
            if num > first:
                third = second
                second = first
                first = num
            elif num > second:
                third = second
                second = num
            elif num > third:
                third = num
        
        return third if third != float('-inf') else first