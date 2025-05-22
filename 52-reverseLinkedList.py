# Day 52 - May 22, 2025
# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/

# Solution
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Solution 1 (Iterative)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        
        while current:
            next_node = current.next  # Save next node
            current.next = prev       # Reverse pointer
            prev = current            # Move prev forward
            current = next_node       # Move current forward
        
        return prev  # New head of the reversed list
    
    # Solution 2 (Recursive)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if head is empty or only one node
        if not head or not head.next:
            return head
        
        # Recursively reverse the rest
        new_head = self.reverseList(head.next)
        
        # Reverse the current node
        head.next.next = head
        head.next = None
        
        return new_head