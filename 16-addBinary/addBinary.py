# Day 16 - March 11, 2025
# 67. Add Binary
# https://leetcode.com/problems/add-binary/

# Solution
def addBinary(a: str, b: str) -> str:
    # Convert binary strings to integers
    int_a = int(a, 2)  # Convert binary string 'a' to an integer
    int_b = int(b, 2)  # Convert binary string 'b' to an integer

    # Sum the integers
    int_sum = int_a + int_b

    # Convert the sum back to a binary string and remove the '0b' prefix
    return bin(int_sum)[2:]

# Example test cases
print(addBinary("11", "1"))      # Output: "100"
print(addBinary("1010", "1011")) # Output: "10101"