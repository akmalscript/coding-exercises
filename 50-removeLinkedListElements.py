# Day 50 - May 18, 2025
# 203. Remove Linked List Elements
# https://leetcode.com/problems/remove-linked-list-elements/

# Solution
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev, curr = dummy, head

        while curr:
            next = curr.next
            if curr.val == val:
                prev.next = next
            else:
                prev = curr
            curr = next
        return dummy.next