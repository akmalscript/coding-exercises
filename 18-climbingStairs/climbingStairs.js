// Day 18 - March 15, 2025
// 70. Climbing Stairs
// https://leetcode.com/problems/climbing-stairs/

// Solutions
class Solution {
    // Solution 1 (Dynamic Programming - Bottom-up Approach)
    static climbStairs(n) {
        if (n === 1) return 1;
        if (n === 2) return 2;

        let prev1 = 2, prev2 = 1;
        for (let i = 3; i <= n; i++) {
            let current = prev1 + prev2;
            prev2 = prev1;
            prev1 = current;
        }

        return prev1;
    }

    // Solution 2 (Recursive with memoization)
    static climbStairs2(n, memo = {}) {
        if (n <= 2) return n;
        if (memo[n]) return memo[n];

        memo[n] = Solution.climbStairs2(n - 1, memo) + Solution.climbStairs2(n - 2, memo);
        return memo[n];
    }

    // Solution 3 (Recursive without memoization)
    static climbStairs3(n) {
        if (n <= 2) return n;
        return Solution.climbStairs3(n - 1) + Solution.climbStairs3(n - 2);
    }
}

// Test cases
console.log("climbStairs");
console.log(Solution.climbStairs(2));  // Output: 2
console.log(Solution.climbStairs(3));  // Output: 3
console.log(Solution.climbStairs(5));  // Output: 8

console.log("climbStairs2");
console.log(Solution.climbStairs2(2));  // Output: 2
console.log(Solution.climbStairs2(3));  // Output: 3
console.log(Solution.climbStairs2(5));  // Output: 8

console.log("climbStairs3");
console.log(Solution.climbStairs3(2));  // Output: 2
console.log(Solution.climbStairs3(3));  // Output: 3
console.log(Solution.climbStairs3(5));  // Output: 8