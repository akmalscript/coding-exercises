// Day 13 - March 5, 2025
// 35. Search Insert Position
// https://leetcode.com/problems/search-insert-position/

// Solution
function searchInsert(nums, target) {
    // Initialize left and right pointers
    let left = 0
    let right = nums.length - 1;

    // Perform binary search
    while (left <= right) {
        let mid = Math.floor((left + right) / 2);  // Find the middle index

        if (nums[mid] === target) {  // If target is found, return its index
            return mid;
        } else if (nums[mid] < target) {  // If target is greater, search the right half
            left = mid + 1;
        } else {  // If target is smaller, search the left half
            right = mid - 1;
        }
    }

    // If target is not found, return the position where it should be inserted
    return left;
}

// Example test cases
console.log(searchInsert([1, 3, 5, 6], 5)); // Output: 2
console.log(searchInsert([1, 3, 5, 6], 2)); // Output: 1
console.log(searchInsert([1, 3, 5, 6], 7)); // Output: 4