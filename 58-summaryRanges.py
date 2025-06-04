# Day 58 - June 3, 2025
# 228. Summary Ranges
# https://leetcode.com/problems/summary-ranges/

# Solution
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        n = len(nums)
        if n == 0:
            return result
        
        start = nums[0]
        
        for i in range(1, n):
            # If the current number is not consecutive
            if nums[i] != nums[i - 1] + 1:
                # Add the range to the result
                if start == nums[i - 1]:
                    result.append(f"{start}")
                else:
                    result.append(f"{start}->{nums[i - 1]}")
                # Update the start to the current number
                start = nums[i]
        
        # Add the last range
        if start == nums[-1]:
            result.append(f"{start}")
        else:
            result.append(f"{start}->{nums[-1]}")
        
        return result