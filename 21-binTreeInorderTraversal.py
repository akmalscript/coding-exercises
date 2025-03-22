# Day 21 - March 21, 2025
# 94. Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Solution
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = leftb
#         self.right = right
class Solution:
    # Solution 1 (Recursive)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
    
    # Solution 2 (Iterative using Stack)
    def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        stack, result = [], []  # Stack for traversal, result list to store values
        current = root  # Start from the root node

        while current or stack:
            # Traverse to the leftmost node
            while current:
                stack.append(current)  # Push current node to the stack
                current = current.left  # Move to the left subtree
            
            # Process the last node from the stack
            current = stack.pop()  # Take the last node
            result.append(current.val)  # Store the node's value
            
            # Move to the right subtree
            current = current.right
        
        return result  # Return the inorder traversal result