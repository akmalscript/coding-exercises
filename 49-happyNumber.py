# Day 49 - May 16, 2025
# 202. Happy Number
# https://leetcode.com/problems/happy-number/

# Solution
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.get_next(n)
        return n == 1
    def get_next(self, number: int) -> int:
        total = 0
        while number > 0:
            digit = number % 10
            total += digit * digit
            number //= 10
        return total