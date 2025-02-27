# Day 7 - February 21, 2025
# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/

# Solution
from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    # If the input array is empty
    if not strs:
        return ""

    # Start with assumption that the longest prefix is ​​the first string
    prefix = strs[0]

    # Compare this prefix with each word in the array
    for string in strs[1:]:
        # Trim the prefix until it matches the start of the current string
        while string[:len(prefix)] != prefix: #  Remove the last character from the prefix
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix

# Example usage:
strs1 = ["flower", "flow", "flight"]
strs2 = ["dog", "racecar", "car"]

print(longestCommonPrefix(strs1))  # Output: "fl"
print(longestCommonPrefix(strs2))  # Output: ""
