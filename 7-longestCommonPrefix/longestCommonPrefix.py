# Day 7 - February 21, 2025
# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/

# Solution
from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    # Jika array kosong
    if not strs:
        return ""

    # Mulai dengan asumsi bahwa prefix terpanjang adalah kata pertama
    prefix = strs[0]

    # Bandingkan prefix ini dengan setiap kata dalam array
    for string in strs[1:]:
        # Potong prefix hingga cocok dengan awal dari string saat ini
        while string[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix

# Contoh penggunaan:
strs1 = ["flower", "flow", "flight"]
strs2 = ["dog", "racecar", "car"]

print(longestCommonPrefix(strs1))  # Output: "fl"
print(longestCommonPrefix(strs2))  # Output: ""
