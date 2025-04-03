# Day 27 - April 2, 2025
# 111. Minimum Depth of Binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Solution
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Solution 1 (BFS)
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([(root, 1)])  # Queue stores nodes along with their depth
        
        while queue:
            node, depth = queue.popleft()
            
            # If we reach a leaf node, return its depth
            if not node.left and not node.right:
                return depth
            
            # Add children to the queue with incremented depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

    # Solution 2 (DFS)
    def minDepth2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # If one of the children is None, we return the depth of the other child + 1
        if not root.left:
            return self.minDepth2(root.right) + 1
        if not root.right:
            return self.minDepth2(root.left) + 1
        
        # If both children exist, return the minimum of both depths
        return min(self.minDepth2(root.left), self.minDepth2(root.right)) + 1