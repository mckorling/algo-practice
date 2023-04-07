# FIND THE PIVOT - Given a sorted array containing only 0s and 1s, return the index of the first number 1.
# eg: Input = [0,0,0,1]
# Output = 3
# Input = [0,1,1,1]
# Output = 1
# Input = [0,0]
# Output = None

# Assumes valid input where num has at least a 0 and 1, or all 1s
def get_pivot(nums):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == 1:
            high = mid - 1
        else:
            low = mid + 1

    return low


nums = [0, 0, 0, 1]
print(get_pivot(nums))
# Output = 3

nums = [0, 1, 1, 1]
print(get_pivot(nums))
# Output = 1

nums = [0, 0, 1, 1, 1]
print(get_pivot(nums))
# Output = 2

nums = [0, 1]
print(get_pivot(nums))
# Output = 1

nums = [0, 0, 0, 1, 1]
print(get_pivot(nums))
# Output = 3

nums = [0, 0, 0, 0, 1]
print(get_pivot(nums))
# Output = 4

nums = [1, 1, 1, 1, 1]
print(get_pivot(nums))
# Output = 0

# nums = [0, 0]
# print(get_pivot(nums))
# Output = None
