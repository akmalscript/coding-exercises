# Day 39 - April 26, 2025
# 169. Majority Element
# https://leetcode.com/problems/majority-element/

# Solution
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)

        return res