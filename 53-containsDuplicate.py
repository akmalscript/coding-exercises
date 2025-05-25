# Day 53 - May 24, 2025
# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/

# Solution
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False