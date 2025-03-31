# Day 26 - March 31, 2025
# 110. Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/

# Solution
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Start the balance check from the root
        return self.check_balance(root) != -1
    
    def check_balance(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0  # Base case: height of an empty tree is 0
        
        # Recursively check the left and right subtrees
        left_height = self.check_balance(node.left)
        right_height = self.check_balance(node.right)
        
        # If the left or right subtree is unbalanced, propagate -1 up the recursion
        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1  # Return -1 to indicate the tree is unbalanced
        
        # Return the height of the current subtree
        return max(left_height, right_height) + 1