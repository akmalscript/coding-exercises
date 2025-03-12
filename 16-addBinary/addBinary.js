// Day 16 - March 11, 2025
// 67. Add Binary
// https://leetcode.com/problems/add-binary/

// Solution
function addBinary(a, b) {
    // Convert binary strings to integers
    let intA = BigInt('0b' + a); // Convert binary string 'a' to BigInt
    let intB = BigInt('0b' + b); // Convert binary string 'b' to BigInt

    // Add the two BigInt numbers
    let sum = intA + intB;

    // Convert the sum back to a binary string and remove the '0b' prefix
    return sum.toString(2);
}

// Example test cases
console.log(addBinary("11", "1"));      // Output: "100"
console.log(addBinary("1010", "1011")); // Output: "10101"