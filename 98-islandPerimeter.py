# Day 98 - August 22, 2025
# 463. Island Perimeter
# https://leetcode.com/problems/island-perimeter/

# Solutions
from typing import List

class Solution:
    # Solution 1 (Iterative Counting)
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        perimeter = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # Each land cell initially contributes 4 sides
                    perimeter += 4
                    
                    # Subtract 2 for each adjacent land cell
                    if r > 0 and grid[r-1][c] == 1:  # check top neighbor
                        perimeter -= 2
                    if c > 0 and grid[r][c-1] == 1:  # check left neighbor
                        perimeter -= 2
                        
        return perimeter

    # Solution 2 (DFS)
    def islandPerimeter2(self, grid: List[List[int]]) -> int:
        visit = set()

        def dfs(i, j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
                return 1
            if (i, j) in visit:
                return 0

            visit.add((i, j))
            perim = dfs(i, j + 1)
            perim += dfs(i + 1, j)
            perim += dfs(i, j - 1)
            perim += dfs(i - 1, j)
            return perim

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)