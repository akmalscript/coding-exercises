# Day 13 - March 5, 2025
# 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position/

# Solution
from typing import List

def search_insert(nums: List[int], target: int) -> int:
    # Initialize left and right pointers
    left = 0
    right = len(nums) - 1

    # Perform binary search
    while left <= right:
        mid = (left + right) // 2  # Find the middle index
        if nums[mid] == target:  # If target is found, return its index
            return mid
        elif nums[mid] < target:  # If target is greater, search the right half
            left = mid + 1
        else:  # If target is smaller, search the left half
            right = mid - 1

    # If target is not found, return the position where it should be inserted
    return left  

# Example test cases
print(search_insert([1, 3, 5, 6], 5))  # Output: 2
print(search_insert([1, 3, 5, 6], 2))  # Output: 1
print(search_insert([1, 3, 5, 6], 7))  # Output: 4