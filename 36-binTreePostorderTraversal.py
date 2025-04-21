# Day 36 - April 20, 2025
# 145. Binary Tree Postorder Traversal
# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Solution
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Solution 1 (Recursive)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postorder(node):
            if not node:
                return []
            return postorder(node.left) + postorder(node.right) + [node.val]
        
        return postorder(root)

    # Solution 2 (Iterative - using two stacks)
    def postorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return result[::-1]  # reverse the result to get postorder