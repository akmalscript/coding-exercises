# Day 68 - June 23, 2025
# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/

# Solution
from typing import List

class Solution:
    # Solution 1 (Two pointers - Overite then fill zeroes)
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_non_zero = 0  # Pointer to track the position to place the next non-zero element

        # First pass: move all non-zero elements to the beginning of the array
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero] = nums[i]
                last_non_zero += 1

        # Second pass: fill the remaining positions with zeroes
        for i in range(last_non_zero, len(nums)):
            nums[i] = 0

    # Solution 2 (Two pointers - Swap)
    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums