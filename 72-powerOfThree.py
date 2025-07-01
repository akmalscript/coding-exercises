# Day 72 - July 1, 2025
# 326. Power of Three
# https://leetcode.com/problems/power-of-three/

# Solutions
class Solution:
    # Solution 1 (Without Loop/Recursion)
    def isPowerOfThree(self, n: int) -> bool:
        # 1162261467 is the largest power of 3 that fits in a 32-bit signed integer (3^19)
        # If n is a positive divisor of 1162261467, then it must be a power of 3
        return n > 0 and 1162261467 % n == 0

    # Solution 2 (With Loop)
    def isPowerOfThree2(self, n: int) -> bool:
        # Return False immediately if n is less than 1
        if n < 1:
            return False
        # Keep dividing n by 3 as long as it is divisible by 3
        while n % 3 == 0:
            n = n // 3
        # If the final result is 1, then n is a power of three
        return n == 1