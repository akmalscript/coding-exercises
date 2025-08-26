# Day 100 - August 26, 2025
# 482. License Key Formatting
# https://leetcode.com/problems/license-key-formatting/

# Solution
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # Remove all dashes and convert to uppercase
        s = s.replace("-", "").upper()
        
        # Determine length of the first group
        first_group_len = len(s) % k or k
        
        # Build result
        result = s[:first_group_len]
        for i in range(first_group_len, len(s), k):
            result += "-" + s[i:i+k]
        
        return result