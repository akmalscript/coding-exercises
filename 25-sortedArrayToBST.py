# Day 25 - March 29, 2025
# 108. Convert Sorted Array to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Solution
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Base case: If no elements left, return None
        if not nums:
            return None

        # Find the middle index
        mid = len(nums) // 2

        # Create a root node with middle value
        root = TreeNode(nums[mid])

        # Recursively build left and right subtrees
        root.left = self.sortedArrayToBST(nums[:mid])  # Left half
        root.right = self.sortedArrayToBST(nums[mid+1:])  # Right half

        return root