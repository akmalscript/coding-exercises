# Day 54 - May 26, 2025
# 219. Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii/

# Solution
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}  # Stores the last seen index of each number
        
        for i, num in enumerate(nums):
            if num in index_map and i - index_map[num] <= k:
                return True
            index_map[num] = i  # Update the last seen index
        
        return False