# Day 19 - March 17, 2025
# 83. Remove Duplicates from Sorted List
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Solution
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # Node value
        self.next = next  # Pointer to the next node

def deleteDuplicates(head: ListNode) -> ListNode:
    current = head  # Pointer to traverse the list
    
    # Traverse the list until we reach the last node
    while current and current.next:
        if current.val == current.next.val:  # Check if next node is a duplicate
            current.next = current.next.next  # Skip the duplicate node
        else:
            current = current.next  # Move to the next distinct node
    
    return head  # Return the updated linked list

# Helper function to create a linked list from a Python list
def create_linked_list(arr):
    if not arr:
        return None  # Return None if the list is empty
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert a linked list back into a Python list
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test cases
test_cases = [
    [1, 1, 2],      # Expected output: [1, 2]
    [1, 1, 2, 3, 3] # Expected output: [1, 2, 3]
]

# Running test cases
for i, test in enumerate(test_cases):
    head = create_linked_list(test)  # Convert list to linked list
    new_head = deleteDuplicates(head)  # Remove duplicates
    result = linked_list_to_list(new_head)  # Convert back to list for verification
    print(f"Input = {test}, Output = {result}")