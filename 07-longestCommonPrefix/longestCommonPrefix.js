// Day 7 - February 21, 2025
// 14. Longest Common Prefix
// https://leetcode.com/problems/longest-common-prefix/

// Solution
function longestCommonPrefix(strs) {
    // If the input array is empty
    if (!strs.length) return "";

    // Start with assumption that the longest prefix is ​​the first string
    let prefix = strs[0];

    // Compare this prefix with each word in the array
    for (let i = 1; i < strs.length; i++) {
        // Trim the prefix until it matches the start of the current string
        while (strs[i].indexOf(prefix) !== 0) {
            prefix = prefix.slice(0, -1); // Remove the last character from the prefix
            if (prefix === "") return "";
        }
    }

    return prefix;
}

// Example usage:
const strs1 = ["flower", "flow", "flight"];
const strs2 = ["dog", "racecar", "car"];

console.log(longestCommonPrefix(strs1)); // Output: "fl"
console.log(longestCommonPrefix(strs2)); // Output: ""
