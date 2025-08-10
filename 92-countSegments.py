# Day 92 - August 10, 2025
# 434. Number of Segments in a String
# https://leetcode.com/problems/number-of-segments-in-a-string/

# Solution
class Solution:
    # Solution 1 (Index-Based Segment Counting)
    def countSegments(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            if (i == 0 or s[i - 1] == " ") and s[i] != " ":
                count += 1
        return count
    
    # Solution 2 (Split-and-Filter Segment Counting)
    def countSegments2(self, s: str) -> int:
        parts = s.split(" ")
        count = 0
        
        for part in parts:
            if part != "":
                count += 1
        
        return count