# Day 87 - July 31, 2025
# 405. Convert a Number to Hexadecimal
# https://leetcode.com/problems/convert-a-number-to-hexadecimal/

# Solution
class Solution:
    def toHex(self, num: int) -> str:
        output = []
        Map = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}
        
        if num == 0:
            return "0"
        
        if num < 0:
            num += 2 ** 32
        
        while num > 0:
            digit = num % 16
            num //= 16
            if digit > 9 and digit < 16:
                digit = Map[digit]
            else:
                digit = str(digit)
            output.append(digit)
        
        return "".join(output[::-1])