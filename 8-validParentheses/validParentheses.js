// Day 7 - February 23, 2025
// 20. Valid Parentheses
// https://leetcode.com/problems/valid-parentheses/

// Solution
function validParentheses(s) {
    let stack = []; // Stack to store opening brackets
    
    for (let char of s) {
        // If the character is an opening bracket, push it onto the stack
        if (char === '(' || char === '{' || char === '[') {
            stack.push(char);
        } else {
            // If the stack is empty but there is a closing bracket, it is invalid (testcase 5)
            if (stack.length === 0) {
                return false;
            }
            // Pop the last element from the stack
            let top = stack.pop();
            // Ensure the closing bracket matches the last opening bracket
            if ((char === ')' && top !== '(') || 
                (char === '}' && top !== '{') || 
                (char === ']' && top !== '[')) {
                return false;
            }
        }
    }

    // If the stack is empty, all brackets are matched correctly
    return stack.length === 0;
}

// Example usage
const testCases = ["()", "()[]{}","([])","(]", "())"];
testCases.forEach(test => {
    console.log(`Input: ${test}, Output: ${validParentheses(test)}`);
});