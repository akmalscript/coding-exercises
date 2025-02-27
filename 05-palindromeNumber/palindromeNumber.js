// Day 5 - February 18, 2025
// 9. Palindrome Number
// https://leetcode.com/problems/palindrome-number/

// Solution
const palindromeNumber = (x) => {
    // Negative numbers cannot be palindromes
    if (x < 0) return false;

    // Store the original value
    let original = x;
    let reversed_number = 0;

    // Reverse the number
    while (x > 0) {
        let last_digit = x % 10;  // Get the last digit
        reversed_number = reversed_number * 10 + last_digit;  // Append the last digit to the reversed number
        x = Math.floor(x / 10);  // Remove the last digit from x
    }

    // Check if the reversed number is the same as the original number
    return reversed_number === original;
}

console.log(palindromeNumber(121))  // Output: true
console.log(palindromeNumber(-121)) // Output: false
console.log(palindromeNumber(10))   // Output: false
