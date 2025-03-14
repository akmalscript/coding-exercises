# Day 17 - March 13, 2025
# 69. Sqrt(x)
# https://leetcode.com/problems/sqrtx/

# Solution - Binary Search
def mySqrt(x: int) -> int:
    # If x is 0 or 1, return x directly as its square root is itself
    if x < 2:
        return x  
    
    # Define the search range: the square root of x cannot be greater than x // 2
    low = 1
    high = x // 2  
    
    while low <= high:
        mid = (low + high) // 2  # Find the middle value
        square = mid * mid  # Compute mid^2
        
        if square == x:  # If mid^2 equals x, return mid
            return mid
        elif square < x:  # If mid^2 is less than x, search in the right half
            low = mid + 1
        else:  # If mid^2 is greater than x, search in the left half
            high = mid - 1  
    
    # high will be the largest integer such that high^2 <= x
    return high  

# Test cases
print(mySqrt(4))  # Output: 2
print(mySqrt(8))  # Output: 2
print(mySqrt(16)) # Output: 4
print(mySqrt(27)) # Output: 5