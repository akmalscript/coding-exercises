# Day 67 - June 21, 2025
# 278. First Bad Version
# https://leetcode.com/problems/first-bad-version/

# Solution
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid  # mid might be the first bad version
            else:
                left = mid + 1  # first bad version must be after mid
        return left  # or right, since left == right