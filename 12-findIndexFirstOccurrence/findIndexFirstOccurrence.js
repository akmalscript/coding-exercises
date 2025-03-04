// Day 12 - March 3, 2025
// 28. Find the Index of the First Occurrence in a String
// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

// Solution
class Solution {
    // Solution 1: Using indexOf()
    static indexFirstOccurrence(haystack, needle) {
        return haystack.indexOf(needle); // indexOf() returns the first index or -1 if not found
    }

    // solution 2: Brute-force method without built-in functions
    static indexFirstOccurrence2(haystack, needle) {
        let haystackLen = haystack.length;
        let needleLen = needle.length;

        // Edge case: If needle is longer than haystack, return -1
        if (needleLen > haystackLen) return -1;

        // Iterate through haystack and check for needle
        for (let i = 0; i <= haystackLen - needleLen; i++) {
            if (haystack.substring(i, i + needleLen) === needle) { // Compare substring
                return i; // Return the index where needle starts
            }
        }

        return -1; // If not found, return -1
    }
}

// Test cases
console.log("indexFirstOccurrence")
console.log(Solution.indexFirstOccurrence("sadbutsad", "sad")) // Output: 0
console.log(Solution.indexFirstOccurrence("leetcode", "leeto")) // Output: -1
console.log(Solution.indexFirstOccurrence("hello", "ll")) // Output: 2
console.log(Solution.indexFirstOccurrence("aaaaa", "bba")) // Output: -1
console.log("indexFirstOccurrence2")
console.log(Solution.indexFirstOccurrence2("sadbutsad", "sad")) // Output: 0
console.log(Solution.indexFirstOccurrence2("leetcode", "leeto")) // Output: -1
console.log(Solution.indexFirstOccurrence2("hello", "ll")) // Output: 2
console.log(Solution.indexFirstOccurrence2("aaaaa", "bba")) // Output: -1