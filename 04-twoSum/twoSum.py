# Day 4 - February 17, 2025
# 1. Two Sum
# https://leetcode.com/problems/two-sum/

# Solution
def twoSum(nums, target):
    n = len(nums)  # length of the list
    for i in range(n):
        for j in range (i+1, n):
            if(nums[i] + nums[j] == target):
                return [i, j]
            
print(twoSum([2,7,11,15], 9))  # Output: [0, 1]
print(twoSum([3,2,4], 6))      # Output: [1, 2]
print(twoSum([3,3], 6))        # Output: [0, 1]