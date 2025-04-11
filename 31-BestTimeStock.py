# Day 31 - April 10, 2025
# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Solution
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Initialize with a very large value
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price  # Update to the lowest price so far
            elif price - min_price > max_profit:
                max_profit = price - min_price  # Update max profit if a better profit is found
        
        return max_profit