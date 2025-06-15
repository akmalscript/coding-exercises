# Day 63 - June 13, 2025
# 257. Binary Tree Paths
# https://leetcode.com/problems/binary-tree-paths/

# Solution
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        paths = []

        def dfs(node, path):
            if not node.left and not node.right:
                paths.append(path)
                return
            if node.left:
                dfs(node.left, path + '->' + str(node.left.val))
            if node.right:
                dfs(node.right, path + '->' + str(node.right.val))

        dfs(root, str(root.val))
        return paths