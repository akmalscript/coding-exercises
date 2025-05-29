# Day 55 - May 28, 2025
# 222. Count Complete Tree Nodes
# https://leetcode.com/problems/count-complete-tree-nodes/

# Solution
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # Function to calculate the height of the leftmost or rightmost path
        def get_height(node, go_left=True):
            height = 0
            while node:
                height += 1
                node = node.left if go_left else node.right
            return height

        if not root:
            return 0

        left_height = get_height(root, go_left=True)
        right_height = get_height(root, go_left=False)

        if left_height == right_height:
            # It's a perfect binary tree, calculate nodes directly
            return (1 << left_height) - 1
        else:
            # Otherwise, count nodes recursively
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)