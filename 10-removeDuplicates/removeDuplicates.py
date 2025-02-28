# Day 10 - February 27, 2025
# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Solution
from typing import List

def removeDuplicates(nums: List[int]) -> int:
    if not nums:
        return 0
    
    # Pointer to track unique elements
    k = 1  
    
    for i in range(1, len(nums)):
        # If the current element is different from the previous one, store it at index k
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1  # Move the unique index forward
            
    return k  # Return the count of unique elements

# Example usage:
nums = [0,0,1,1,1,2,2,3,3,4]
k = removeDuplicates(nums)
print(k)  # Output: 5
print(nums[:k])  # Output: [0, 1, 2, 3, 4]