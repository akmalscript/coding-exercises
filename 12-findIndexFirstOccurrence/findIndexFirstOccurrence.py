# Day 12 - March 3, 2025
# 28. Find the Index of the First Occurrence in a String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

# Solution
class Solution:
  # Solution 1:  Using find()
  def indexFirstOccurrence(haystack: str, needle: str) -> int:
    return haystack.find(needle)  # `find()` returns the first index or -1 if not found

  # solution 2: Brute-force method without built-in functions
  def indexFirstOccurrence2(haystack: str, needle: str) -> int:
    haystack_len: int = len(haystack)
    needle_len: int = len(needle)

    # Edge case: If needle is longer than haystack, it's impossible to find it
    if needle_len > haystack_len:
        return -1

    # Iterate through haystack and check for needle
    for i in range(haystack_len - needle_len + 1):  
        if haystack[i:i + needle_len] == needle:  # Compare substring
            return i  # Return the index where needle starts

    return -1  # If not found, return -1

# Test cases
print("indexFirstOccurrence")
print(Solution.indexFirstOccurrence("sadbutsad", "sad"))  # Output: 0
print(Solution.indexFirstOccurrence("leetcode", "leeto"))  # Output: -1
print(Solution.indexFirstOccurrence("hello", "ll"))  # Output: 2
print(Solution.indexFirstOccurrence("aaaaa", "bba"))  # Output: -1
print("indexFirstOccurrence2")
print(Solution.indexFirstOccurrence2("sadbutsad", "sad"))  # Output: 0
print(Solution.indexFirstOccurrence2("leetcode", "leeto"))  # Output: -1
print(Solution.indexFirstOccurrence2("hello", "ll"))  # Output: 2
print(Solution.indexFirstOccurrence2("aaaaa", "bba"))  # Output: -1