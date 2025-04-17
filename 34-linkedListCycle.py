# Day 34 - April 16, 2025
# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/

# Solution (Floyd's Cycle Detection || Tortoise and Hare)
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True  # Cycle detected

        return False  # No cycle