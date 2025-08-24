# Day 99 - August 24, 2025
# 476. Number Complement
# https://leetcode.com/problems/number-complement/

# Solution
class Solution:
    def findComplement(self, num: int) -> int:
        # Find the bit length of the number
        length = len(bin(num)) - 2   # bin(num) returns a string like '0b101'
        
        # Build a mask with all bits = 1
        mask = 0
        for i in range(length):
            mask = mask * 2 + 1   # add 1 to the end of the mask bits
        
        # Flip bits using XOR
        result = num ^ mask
        return result