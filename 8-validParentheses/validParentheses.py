# Day 7 - February 23, 2025
# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

# Solution
def validParentheses(s: str) -> bool:
    stack = []  # Use a stack to store opening brackets
    
    for char in s:
        # If the character is an opening bracket, push it onto the stack
        if char == '(' or char == '{' or char == '[':
            stack.append(char)
        else:
            # If the stack is empty but there is a closing bracket, it is invalid (testcase 5)
            if not stack:
                return False
            # Pop the last element from the stack
            top = stack.pop()
            # Ensure the closing bracket matches the last opening bracket
            if (char == ')' and top != '(') or \
               (char == '}' and top != '{') or \
               (char == ']' and top != '['):
                return False
    
    # If the stack is empty, all brackets are matched correctly
    return len(stack) == 0

# Example usage
test_cases = ["()", "()[]{}","([])","(]", "())"]
for test in test_cases:
    print(f"Input: {test}, Output: {validParentheses(test)}")