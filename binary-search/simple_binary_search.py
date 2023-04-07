# VANILLA BINARY SEARCH - Given a sorted array and a target, return the index of the target.
# eg: Input = [2,5,9,10,16], 10
# Output = 3 (index of 10)
# Input= [-10, -3, 0, 20, 22], -3
# Output = 1 (index of -3)
# Input = [3,6,10,15], 20
# Output = None (target not found)

def binary_search(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        print(f"low: {low}, high: {high}")
        mid = (low + high) // 2
        print(f"mid: {mid}")
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return None


# nums = [2, 5, 9, 10, 16]
# target = 10
# print(binary_search(nums, target))
# # Output = 3 (index of 10)

nums = [-10, -3, 0, 20, 22]
target = -3
print(binary_search(nums, target))
# Output = 1 (index of -3)

# nums = [3, 6, 10, 15]
# target = 20
# print(binary_search(nums, target))
# # Output = None (target not found)
