# Day 38 - April 24, 2025
# 168. Excel Sheet Column Title
# https://leetcode.com/problems/excel-sheet-column-title/

# Solution
class Solution:
    # Solution 1 (string concatenation approach)
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber > 0:
            offset = (columnNumber - 1) % 26
            res += chr(ord('A') + offset)
            columnNumber = (columnNumber - 1) // 26

        return res[::-1] # reverse
    
    # Solution 2 (list-buffer approach)
    def convertToTitle2(self, columnNumber: int) -> str:
        title_chars = []

        # Repeatedly extract the least‑significant “digit”
        while columnNumber > 0:
            columnNumber -= 1                    # shift to 0‑based indexing
            remainder = columnNumber % 26        # current digit (range 0–25, mapping to A–Z)
            title_chars.append(chr(ord('A') + remainder))
            columnNumber //= 26                  # move to the next “digit”

        # The characters were collected from least‑ to most‑significant;
        # reverse them to obtain the final title.
        return ''.join(reversed(title_chars))