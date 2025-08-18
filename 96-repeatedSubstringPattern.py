# Day 96 - August 18, 2025
# 459. Repeated Substring Pattern
# https://leetcode.com/problems/repeated-substring-pattern/

# Solution
class Solution:
    # Solution 1 (Trick Method)
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]

    # Solution 2 (KMP prefix function Algorithm)
    def repeatedSubstringPattern2(self, s: str) -> bool:
        n = len(s)
        lps = [0] * n  # Longest Prefix Suffix array
        j = 0  # length of the previous longest prefix suffix

        # Build the LPS array
        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = lps[j - 1]
            if s[i] == s[j]:
                j += 1
                lps[i] = j

        l = lps[-1]  # length of the longest proper prefix which is also a suffix
        return l != 0 and n % (n - l) == 0