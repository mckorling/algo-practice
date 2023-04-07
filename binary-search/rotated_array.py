# ROTATED ARRAY -  A sorted array (ex [1,2,3,4,5,6]) was split into two arrays (ex [1,23] and [4,5,6])
# and then flip flopped and put back together (in this example[4,5,6,1,2,3]).
# Given a target number, return the index of the target in this now rotated array.

# So assuming array is always split in half at the halfway point (length // 2)
# Can do binary search on each half of the array?
# Or add another check to the if statements
#

# Input = [4,5,6,1,2,3], 2
# Output = 4 (index of 2)
# Input = [9, 2, 6], 9
# Output = 0 (index of 9)
# Input = [1,2,3,-6,-5], 4
# Output = None (target not found)

# Goal: O(logn) time complexity
# CAN'T sort array and then search (O(nlogn))
# CAN'T find how much it is rotated by (O(n))
# Find where to split the array and search that half

def get_rotated_index(nums, target):
    pass


# Originally: [1, 2, 3, 4, 5, 6] -> [1, 2, 3] <-> [4, 5, 6]
nums = [4, 5, 6, 1, 2, 3]
print(get_rotated_index(nums, 2))
# Output = 4 (index of 2)

nums = [9, 2, 6]  # Originally: [2, 6, 9] -> [2, 6] <-> [9]
print(get_rotated_index(nums, 9))
# Output = 0 (index of 9)

# Originally: [-6, -5, 1, 2, 3] -> [-6, -5] <-> [1, 2, 3]
nums = [1, 2, 3, -6, -5]
print(get_rotated_index(nums, 4))
# Output = None (target not found)

# Originally: [-6, -5, 1, 2, 3] -> [-6, -5] <-> [1, 2, 3]
nums = [1, 2, 3, -6, -5]
print(get_rotated_index(nums, -5))
# Output = None (target not found)


# O(n) solution, where -1 is returned if the target number is not in num
def get_rotated_index_linear(nums, target):
    for index, num in enumerate(nums):
        if num == target:
            return index
    return -1


# Originally: [-6, -5, 1, 2, 3] -> [-6, -5] <-> [1, 2, 3]
nums = [1, 2, 3, -6, -5]
print(get_rotated_index_linear(nums, 3))
# Output = 2

# Originally: [-6, -5, 1, 2, 3] -> [-6, -5] <-> [1, 2, 3]
nums = [1, 2, 3, -6, -5]
print(get_rotated_index_linear(nums, 10))
# Output = None (target not found)
