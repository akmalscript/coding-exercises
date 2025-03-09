# Day 15 - March 9, 2025
# 66. Plus One
# https://leetcode.com/problems/plus-one/

# Solution
def plusOne(digits: list[int]) -> list[int]:
    n = len(digits)

    # Traverse from the last digit to the first
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:  # If the digit is not 9, increment it by 1
            digits[i] += 1
            return digits  # Return the updated digits

        digits[i] = 0  # If the digit is 9, set it to 0 and continue to the previous digit

    # If all digits were 9, we need to add an extra 1 at the beginning
    return [1] + digits


# Example test cases
print(plusOne([1, 2, 3]))  # Output: [1, 2, 4]
print(plusOne([4, 3, 2, 1]))  # Output: [4, 3, 2, 2]
print(plusOne([9]))  # Output: [1, 0]