# Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in non-decreasing order,
# find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.
# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]
# Constraints:
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# nums is a non-decreasing array.
# -10^9 <= target <= 10^9

# two pointer
def find_first_and_last2(nums, target):
    low = 0
    high = len(nums) - 1
    low_i = None
    high_i = None
    while low <= high:
        print(f"{nums[low]}, {nums[high]}")
        if nums[low] != target:
            low += 1
        else:
            if low_i is None:
                low_i = low

        if nums[high] != target:
            high -= 1
        else:
            if high_i is None:
                high_i = high
        # quit when done
        if low_i != None and high_i != None:
            return [low_i, high_i]

    return [-1, -1]


# binary search
def find_first_and_last(nums, target):
    low = 0
    high = len(nums)
    while low <= high:
        mid = (low + high) // 2
        # need to divide space in two but track two different pointers....


# Example 1:
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(find_first_and_last(nums, target))
# Output: [3,4]

# Example 2:
nums = [5, 7, 7, 8, 8, 10]
target = 6
print(find_first_and_last(nums, target))
# Output: [-1,-1]

# Example 3:
nums = []
target = 0
print(find_first_and_last(nums, target))
# Output: [-1,-1]
