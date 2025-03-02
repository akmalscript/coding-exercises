# Day 11 - March 1, 2025
# 27. Remove Element
# https://leetcode.com/problems/remove-element/

# Solution
from typing import List

def removeElement(nums: List[int], val: int) -> int:
    k = 0  # Pointer for placing non-val elemetns
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

# Example usage:
nums = [3, 2, 2, 3]
val = 3
k = removeElement(nums, val)
print(k)  # Output: 2
print(nums[:k])  # Output: [2, 2]