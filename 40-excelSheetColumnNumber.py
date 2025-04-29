# Day 40 - April 28, 2025
# 171. Excel Sheet Column Number
# https://leetcode.com/problems/excel-sheet-column-number/

# Solution
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            result = result * 26 + (ord(char) - ord('A') + 1)
        return result