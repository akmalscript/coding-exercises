// Day 14 - March 7, 2025
// 58. Length of Last Word
// https://leetcode.com/problems/length-of-last-word/

// Solution
class Solution {
    // Solution 1 (Using built-in methods)
    static lengthOfLastWord(s) {
        return s.trim().split(" ").pop().length;
    }

    // Solution 2 (Without built-in trim/split/pop except length)
    static lengthOfLastWord2(s) {
        let length = 0;
        let i = s.length - 1;

        // Skip spaces at the end of the string
        while (i >= 0 && s[i] === ' ') {
            i--;
        }

        // Count the length of the last word
        while (i >= 0 && s[i] !== ' ') {
            length++;
            i--;
        }

        return length;
    }
}

// Test cases
console.log("lengthOfLastWord");
console.log(Solution.lengthOfLastWord("Hello World"));       // Output: 5
console.log(Solution.lengthOfLastWord("   fly me   to   the moon  "));  // Output: 4
console.log(Solution.lengthOfLastWord("luffy is still joyboy"));  // Output: 6
console.log(Solution.lengthOfLastWord("a "));  // Output: 1

console.log("lengthOfLastWord2");
console.log(Solution.lengthOfLastWord2("Hello World"));       // Output: 5
console.log(Solution.lengthOfLastWord2("   fly me   to   the moon  "));  // Output: 4
console.log(Solution.lengthOfLastWord2("luffy is still joyboy"));  // Output: 6
console.log(Solution.lengthOfLastWord2("a "));  // Output: 1
