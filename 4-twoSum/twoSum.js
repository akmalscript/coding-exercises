// Day 4 - February 17, 2025
// 1. Two Sum
// https://leetcode.com/problems/two-sum/

// Solution
const twoSum = (nums, target) => {
    const n = nums.length;  // length of the list

    for(let i = 0; i < n; i ++) {
        for(let j = i+1; j < n; j ++) {
            if(nums[i] + nums[j] === target) {
                return [i, j];
            }
        }
    }
}

console.log(twoSum([2,7,11,15], 9))  // Output: [0, 1]
console.log(twoSum([3,2,4], 6))      // Output: [1, 2]
console.log(twoSum([3,3], 6))        // Output: [0, 1]