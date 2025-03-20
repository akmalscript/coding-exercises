# Day 20 - March 19, 2025
# 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/

# Solution
def merge(nums1, m, nums2, n):
    # Pointers for the last elements in nums1, nums2, and the last position in nums1
    i, j, k = m - 1, n - 1, m + n - 1  

    # Merge elements from the back to avoid shifting
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:  
            nums1[k] = nums1[i]  # Place the larger value at the correct position
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1  

    # Copy any remaining elements from nums2 (if any)
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

# Example Usage
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

merge(nums1, m, nums2, n)
print(nums1)  # Output: [1,2,2,3,5,6]