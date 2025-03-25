# Day 23 - March 25, 2025
# 101. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/

# Solution
from typing import Optional
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Solution 1 (Recursive)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSymmetric(self, root: Optional[TreeNode]) -> bool:
            """ Checks if a binary tree is symmetric (mirror of itself). """
            if not root:
                return True  # An empty tree is symmetric
            return self.isMirror(root.left, root.right)
        
        def isMirror(self, t1: TreeNode, t2: TreeNode) -> bool:
            """ Helper function to check if two trees are mirror images. """
            if not t1 and not t2:
                return True  # Both subtrees are empty, so they are symmetric
            if not t1 or not t2:
                return False  # If one subtree is empty and the other is not, it's not symmetric
            
            # Check if current nodes have the same value and their children are mirrors
            return (t1.val == t2.val) and self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left)
    
    # Solution 2 (Iterative using Queue)
    def isSymmetric2(self, root: Optional[TreeNode]) -> bool:
        """ Iteratively checks if a binary tree is symmetric using a queue. """
        if not root:
            return True  # An empty tree is symmetric
        
        # Initialize a queue with the left and right subtrees
        queue = deque([(root.left, root.right)])
        
        while queue:
            t1, t2 = queue.popleft()  # Get the next two nodes to compare
            
            if not t1 and not t2:
                continue  # Both are None, so they are symmetric at this level
            
            if not t1 or not t2 or t1.val != t2.val:
                return False  # If they are not equal, tree is not symmetric
            
            # Add child nodes in mirrored order
            queue.append((t1.left, t2.right))  # Compare left subtree of t1 with right subtree of t2
            queue.append((t1.right, t2.left))  # Compare right subtree of t1 with left subtree of t2
        
        return True  # If all levels are symmetric, return True