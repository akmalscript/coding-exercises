// Day 19 - March 17, 2025
// 83. Remove Duplicates from Sorted List
// https://leetcode.com/problems/remove-duplicates-from-sorted-list/

// Solution
// Definition for singly-linked list
class ListNode {
    constructor(val = 0, next = null) {
        this.val = val;   // Node value
        this.next = next; // Pointer to next node
    }
}

// Function to remove duplicates from a sorted linked list
const deleteDuplicates = (head) => {
    let current = head;

    // Traverse the list and remove duplicates
    while (current && current.next) {
        if (current.val === current.next.val) {
            current.next = current.next.next; // Skip duplicate node
        } else {
            current = current.next; // Move to the next node
        }
    }
    
    return head; // Return updated list
};

// Helper function to create a linked list from an array
const createLinkedList = (arr) => {
    if (arr.length === 0) return null;
    let head = new ListNode(arr[0]);
    let current = head;
    for (let i = 1; i < arr.length; i++) {
        current.next = new ListNode(arr[i]);
        current = current.next;
    }
    return head;
};

// Helper function to convert a linked list back to an array
const linkedListToArray = (head) => {
    let result = [];
    let current = head;
    while (current) {
        result.push(current.val);
        current = current.next;
    }
    return result;
};

// Test cases
const testCases = [
    [1, 1, 2],      // Expected output: [1, 2]
    [1, 1, 2, 3, 3] // Expected output: [1, 2, 3]
];

// Running test cases
testCases.forEach((test, index) => {
    let head = createLinkedList(test);  // Convert array to linked list
    let newHead = deleteDuplicates(head); // Remove duplicates
    let result = linkedListToArray(newHead); // Convert back to array
    console.log(`Input = ${test}, Output = ${result}`);
});
