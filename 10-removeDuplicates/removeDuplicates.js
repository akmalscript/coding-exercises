// Day 10 - February 27, 2025
// 26. Remove Duplicates from Sorted Array
// https://leetcode.com/problems/remove-duplicates-from-sorted-array/

// Solution
const removeDuplicates = (nums) => {
    if (nums.length === 0) return 0;
    
    // Pointer to track unique elements
    let k = 1;  

    for (let i = 1; i < nums.length; i++) {
        // If the current element is different from the previous one, store it at index k
        if (nums[i] !== nums[i - 1]) {
            nums[k] = nums[i];
            k++;  // Move the unique index forward
        }
    }

    return k; // Return the count of unique elements
};

// Example usage:
let nums = [0,0,1,1,1,2,2,3,3,4];
let k = removeDuplicates(nums);
console.log(k);  // Output: 5
console.log(nums.slice(0, k));  // Output: [0, 1, 2, 3, 4]