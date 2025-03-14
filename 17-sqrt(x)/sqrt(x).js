// Day 17 - March 13, 2025
// 69. Sqrt(x)
// https://leetcode.com/problems/sqrtx/

// Solution - Binary Search
function mySqrt(x) {
    if (x < 2) return x; // If x is 0 or 1, return x directly
    
    let low = 1, high = Math.floor(x / 2);
    
    while (low <= high) {
        let mid = Math.floor((low + high) / 2);
        let square = mid * mid;
        
        if (square === x) return mid; // If mid^2 equals x, return mid
        else if (square < x) low = mid + 1; // Search in the right half
        else high = mid - 1; // Search in the left half
    }
    
    return high; // high is the largest integer such that high^2 <= x
}

// Test cases
console.log(mySqrt(4));  // Output: 2
console.log(mySqrt(8));  // Output: 2
console.log(mySqrt(16)); // Output: 4
console.log(mySqrt(27)); // Output: 5