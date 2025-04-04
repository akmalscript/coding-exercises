# Day 28 - April 4, 2025
# 112. Path Sum
# https://leetcode.com/problems/path-sum/

# Solution
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Base case: if the tree is empty
        if not root:
            return False
        
        # If it's a leaf node, check if the value matches the targetSum
        if not root.left and not root.right:
            return root.val == targetSum
        
        # Recursively check the left and right subtrees with the updated target sum
        remainingSum = targetSum - root.val
        return self.hasPathSum(root.left, remainingSum) or self.hasPathSum(root.right, remainingSum)