# Day 35 - April 18, 2025
# 144. Binary Tree Preorder Traversal
# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Solution
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Solution 1 (Iterative - using a stack)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack, output = [root], []

        while stack:
            node = stack.pop()
            if node:
                output.append(node.val)
                # Push right child first so that left is processed first
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        
        return output
    
    # Solution 2 (Recursive)
    def preorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node: Optional[TreeNode]):
            if not node:
                return
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        result = []
        dfs(root)
        return result