# Day 8 - February 25, 2025
# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

# Solution
# Definition for a singly linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # Node value
        self.next = next  # Pointer to the next node

def mergeTwoLists(list1, list2):
    dummy = ListNode()  # Create a dummy node to simplify the merging process
    current = dummy  # Pointer to build the merged list

    while list1 and list2:  # Loop while both lists have elements
        if list1.val < list2.val:
            current.next = list1  # Append the smaller node from list1
            list1 = list1.next  # Move to the next node in list1
        else:
            current.next = list2  # Append the smaller or equal node from list2
            list2 = list2.next  # Move to the next node in list2
        current = current.next  # Move the pointer forward

    current.next = list1 if list1 else list2  # Append the remaining nodes

    return dummy.next  # Return the merged list starting from the first real node

# Function to convert an array to a linked list
def arrayToLinkedList(arr):
    if not arr:
        return None  # Return None if the array is empty
    head = ListNode(arr[0])  # Create the head node
    current = head
    for val in arr[1:]:  # Iterate through the array to create nodes
        current.next = ListNode(val)
        current = current.next
    return head

# Function to convert a linked list to an array
def linkedListToArray(node):
    result = []
    while node:
        result.append(node.val)  # Append each node's value to the array
        node = node.next
    return result

# Example input as arrays
arr1 = [1, 2, 4]
arr2 = [1, 3, 4]

# Convert arrays to linked lists
list1 = arrayToLinkedList(arr1)
list2 = arrayToLinkedList(arr2)

# Merge the linked lists
merged_list = mergeTwoLists(list1, list2)

# Convert the merged linked list back to an array
result = linkedListToArray(merged_list)

# Print the output
print(result)