# Day 77 - July 11, 2025
# 349. Intersection of Two Arrays
# https://leetcode.com/problems/intersection-of-two-arrays/

# Solution
from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set(nums1)  # Convert nums1 to a set for O(1) lookups
        res = []
        # Iterate through nums2 and check for intersection
        for n in nums2:
            if n in seen:
                res.append(n)      # Add to result if present in seen
                seen.remove(n)     # Remove to ensure uniqueness
        return res