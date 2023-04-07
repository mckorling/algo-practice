# Peak Index in a Mountain Array
# An array arr is a mountain if the following properties hold:
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given a mountain array arr, return the index i such that
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].
# You must solve it in O(log(arr.length)) time complexity.
# Example 1:
# Input: arr = [0,1,0]
# Output: 1
# Example 2:
# Input: arr = [0,2,1,0]
# Output: 1
# Example 3:
# Input: arr = [0,10,5,2]
# Output: 1
# Constraints:
# 3 <= arr.length <= 10^5
# 0 <= arr[i] <= 10^6
# arr is guaranteed to be a mountain array.

# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/

# Mountain =
# 1: minimum length of 3
# 2: there is some index i that needs to be returned
# 3: all numbers before i are lower value in ascending order
# 4: all numbers after i are lower value in descending order
def find_peak(nums):
    low = 0
    high = len(nums) - 1
    while low <= high:
        # get mid point
        mid = (low + high) // 2
        if mid == 0:
            mid = 1
        # if mid is the start or end of the nums arr, there is no mountain
        # technically this isn't need because the constraints guarantee a mtn arr
        # if mid <= 0 or mid + 1 >= len(nums):
        #     return -1
        print(f"mid index: {mid}, nums at mid: {nums[mid]}")
        print(f"low: {low}, high: {high}")
        # peak is the point that is greater than that to the left and to the right
        if nums[mid-1] < nums[mid] > nums[mid+1]:
            return mid
        # figure out if mid is in the first half ascending
        # which means that peak is to the right
        elif nums[mid-1] < nums[mid] < nums[mid+1]:
            low = mid + 1
        # else it is in the second half descending
        else:
            high = mid - 1
        print(f"end of while loop: low: {low}, high: {high}")
    return -1


# needed to add check for if mid is 0 to pass
arr = [3, 9, 8, 6, 4]
print(find_peak(arr))
# Output: 1
a = {{1, 2, 3}}
if {2, 3, 1} not in a:
    a.add({2, 3, 1})
print(a)
# arr = [3, 4, 5, 1]
# print(find_peak(arr))
# Output: 2


# Example 1:
# arr = [0, 1, 0]
# print(find_peak(arr))
# # Output: 1

# # Example 2:
# arr = [0, 2, 1, 0]
# print(find_peak(arr))
# # Output: 1

# # Example 3:
# arr = [0, 10, 5, 2]
# print(find_peak(arr))
# Output: 1
