# Day 70 - June 27, 2025
# 292. Nim Game
# https://leetcode.com/problems/nim-game/

# Solution
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0