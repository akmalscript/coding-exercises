# Day 14 - March 7, 2025
# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/

# Solution
class Solution:
    # Solution 1 (Using built-in methods)
    def lengthOfLastWord(s: str) -> int:
        return len(s.strip().split()[-1])
    
    # Solution 2 (Without built-in trim/split/pop except length)
    def lengthOfLastWord2(s: str) -> int:
        length = 0
        i = len(s) - 1

        # Skip spaces at the end of string
        while i >= 0 and s[i] == ' ':
            i -= 1

        # Count the length of the last word
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        return length

# Test cases
print("lengthOfLastWord")
print(Solution.lengthOfLastWord("Hello World"))       # Output: 5
print(Solution.lengthOfLastWord("   fly me   to   the moon  "))  # Output: 4
print(Solution.lengthOfLastWord("luffy is still joyboy"))  # Output: 6
print(Solution.lengthOfLastWord("a "))  # Output: 1

print("lengthOfLastWord2")
print(Solution.lengthOfLastWord2("Hello World"))       # Output: 5
print(Solution.lengthOfLastWord2("   fly me   to   the moon  "))  # Output: 4
print(Solution.lengthOfLastWord2("luffy is still joyboy"))  # Output: 6
print(Solution.lengthOfLastWord2("a "))  # Output: 1