# Day 94 - August 14, 2025
# 448. Find All Numbers Disappeared in an Array
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

# Solution
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Step 1: Mark each number's corresponding index as visited
        for n in nums:
            i = abs(n) - 1
            nums[i] = -1 * abs(nums[i])

        # Step 2: Collect indices whose values are still positive
        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)

        # Step 3: Return all missing numbers
        return res