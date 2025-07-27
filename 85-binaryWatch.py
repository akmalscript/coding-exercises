# Day 85 - July 27, 2025
# 401. Binary Watch
# https://leetcode.com/problems/binary-watch/

# Solution
from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        for hour in range(12):  # 0 to 11
            for minute in range(60):  # 0 to 59
                # Count the number of '1's in the combined binary string
                if bin(hour).count('1') + bin(minute).count('1') == turnedOn:
                    result.append(f"{hour}:{minute:02d}")
        return result