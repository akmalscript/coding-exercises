# Day 79 - July 15, 2025
# 367. Valid Perfect Square
# https://leetcode.com/problems/valid-perfect-square/

# Solutions
class Solution:
    # Solution 1
    def isPerfectSquare(self, num: int) -> bool:
        # Binary search method: O(log n)
        l, r = 1, num
        while l <= r:
            mid = (l + r) // 2
            if mid * mid > num:
                r = mid - 1
            elif mid * mid < num:
                l = mid + 1
            else:
                return True
        return False

    # Solution 2
    def isPerfectSquare2(self, num: int) -> bool:
        # Brute-force method: O(sqrt(n))
        for i in range(1, num + 1):
            if i * i == num:
                return True
            if i * i > num:
                return False
