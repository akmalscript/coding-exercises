// Day 20 - March 19, 2025
// 88. Merge Sorted Array
// https://leetcode.com/problems/merge-sorted-array/

// Solution
function merge(nums1, m, nums2, n) {
    let i = m - 1; // Pointer for nums1
    let j = n - 1; // Pointer for nums2
    let k = m + n - 1; // Pointer for the last position in nums1

    // Merge elements from the end to avoid shifting
    while (i >= 0 && j >= 0) {
        if (nums1[i] > nums2[j]) {
            nums1[k] = nums1[i]; // Place the larger value at the correct position
            i--;
        } else {
            nums1[k] = nums2[j];
            j--;
        }
        k--;
    }

    // Copy any remaining elements from nums2 (if any)
    while (j >= 0) {
        nums1[k] = nums2[j];
        j--;
        k--;
    }
}

// Example Usage
let nums1 = [1, 2, 3, 0, 0, 0];
let m = 3;
let nums2 = [2, 5, 6];
let n = 3;

merge(nums1, m, nums2, n);
console.log(nums1); // Output: [1, 2, 2, 3, 5, 6]