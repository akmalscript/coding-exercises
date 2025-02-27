# Day 6 - February 19, 2025
# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/

# Solution
def romanToInt(s: str) -> int:
    # Mapping of Roman numerals to integer values
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    # Initialize total and previous value
    total = 0
    prev_value = 0

    # Loop through the characters from right to left
    for char in reversed(s):
        # Get the integer value of the current Roman numeral
        value = roman[char]
        
        # If the current value is less than the previous value,
        # it means we should subtract it (e.g., IV = 4, IX = 9)
        if value < prev_value:
            total -= value
        else:
            # Otherwise, add the value to the total
            total += value
        
        # Update the previous value for the next iteration
        prev_value = value

    # Return the total as the final result
    return total

print(romanToInt("III"))      # Output: 3
print(romanToInt("LVIII"))    # Output: 58
print(romanToInt("MCMXCIV"))  # Output: 1994
