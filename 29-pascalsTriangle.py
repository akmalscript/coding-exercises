# Day 29 - April 6, 2025
# 118. Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/

# Solution
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        
        for i in range(numRows):
            row = [1] * (i + 1)  # Create a row filled with 1s
            for j in range(1, i):  # Compute inner elements
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)
        
        return triangle