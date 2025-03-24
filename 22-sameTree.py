# Day 22 - March 23, 2025
# 100. Same Tree
# https://leetcode.com/problems/same-tree/

# Solution
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both nodes are None, trees are identical
        if not p and not q:
            return True
        # If one is None but the other isn't, trees are different
        if not p or not q:
            return False
        # If values are different, trees are different
        if p.val != q.val:
            return False
        # Recursively check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)