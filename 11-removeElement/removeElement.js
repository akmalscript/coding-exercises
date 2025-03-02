// Day 11 - March 1, 2025
// 27. Remove Element
// https://leetcode.com/problems/remove-element/

// Solution
const removeElement = (nums, val) => {
    let k = 0; // Pointer for placing non-val elements
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== val) {
            nums[k] = nums[i];
            k++;
        }
    }
    return k;
}

// Example usage:
let nums = [3, 2, 2, 3];
let val = 3;
let k = removeElement(nums, val);
console.log(k);       // Output: 2
console.log(nums.slice(0, k)); // Output: [2, 2]
