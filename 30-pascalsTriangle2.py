# Day 30 - April 8, 2025
# 119. Pascal's Triangle II
# https://leetcode.com/problems/pascals-triangle-ii/

# Solution
from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)
        for i in range(1, rowIndex):
            for j in range(i, 0, -1):
                row[j] += row[j - 1]
        return row