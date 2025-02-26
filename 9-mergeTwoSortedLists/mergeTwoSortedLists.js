// Day 8 - February 25, 2025
// 21. Merge Two Sorted Lists
// https://leetcode.com/problems/merge-two-sorted-lists/

// Solution
// Definition for a singly linked list node
class ListNode {
    constructor(val = 0, next = null) {
        this.val = val; // Node value
        this.next = next; // Pointer to the next node
    }
}

// Function to merge two sorted linked lists
function mergeTwoLists(list1, list2) {
    let dummy = new ListNode(); // Create a dummy node to simplify the merging process
    let current = dummy; // Pointer to build the merged list

    while (list1 !== null && list2 !== null) { // Loop while both lists have elements
        if (list1.val < list2.val) {
            current.next = list1; // Append the smaller node from list1
            list1 = list1.next; // Move to the next node in list1
        } else {
            current.next = list2; // Append the smaller or equal node from list2
            list2 = list2.next; // Move to the next node in list2
        }
        current = current.next; // Move the pointer forward
    }

    // Append remaining nodes if any list is not empty
    current.next = list1 !== null ? list1 : list2;

    return dummy.next; // Return the merged list (ignoring dummy node)
}

// Function to convert an array to a linked list
function arrayToLinkedList(arr) {
    if (arr.length === 0) return null;
    let head = new ListNode(arr[0]);
    let current = head;
    for (let i = 1; i < arr.length; i++) {
        current.next = new ListNode(arr[i]);
        current = current.next;
    }
    return head;
}

// Function to convert a linked list to an array (for easy output)
function linkedListToArray(node) {
    let result = [];
    while (node !== null) {
        result.push(node.val);
        node = node.next;
    }
    return result;
}

// Example input
let arr1 = [1, 2, 4];
let arr2 = [1, 3, 4];

// Convert arrays to linked lists
let list1 = arrayToLinkedList(arr1);
let list2 = arrayToLinkedList(arr2);

// Merge the lists
let mergedList = mergeTwoLists(list1, list2);

// Convert merged linked list back to array
console.log(linkedListToArray(mergedList)); // Output: [1, 1, 2, 3, 4, 4]
