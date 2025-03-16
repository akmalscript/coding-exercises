# Day 18 - March 15, 2025
# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/

# Solutions
from functools import lru_cache

class Solution:
    # Solution1 (Dynamic Programming - Bottom-up Approach)
    def climbStairs(n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        prev1, prev2 = 2, 1
        for i in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        
        return prev1
    
    # Solution 2 (Recursive with memorization)
    @lru_cache(None)
    def climbStairs2(n):
        if n <= 2:
            return n
        return Solution.climbStairs2(n-1) + Solution.climbStairs2(n-2)
    
    # Solution 3 (Recursive without memorization)
    def climbStairs3(n):
        if n <= 2:
            return n
        return Solution.climbStairs3(n-1) + Solution.climbStairs3(n-2)


    


# Test cases
print("climbStairs")
print(Solution.climbStairs(2))  # Output: 2
print(Solution.climbStairs(3))  # Output: 3
print(Solution.climbStairs(5))  # Output: 8

print("climbStairs2")
print(Solution.climbStairs2(2))  # Output: 2
print(Solution.climbStairs2(3))  # Output: 3
print(Solution.climbStairs2(5))  # Output: 8

print("climbStairs3")
print(Solution.climbStairs3(2))  # Output: 2
print(Solution.climbStairs3(3))  # Output: 3
print(Solution.climbStairs3(5))  # Output: 8