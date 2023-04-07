# Fruit Into Baskets
# You are visiting a farm that has a single row of fruit trees arranged from left to right.
# The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.
# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:
# You only have two baskets, and each basket can only hold a single type of fruit.
# There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree
# (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.
# Example 1:
# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.
# Example 2:
# Input: fruits = [0,1,2,2]
# Output: 3
# Explanation: We can pick from trees [1,2,2].
# If we had started at the first tree, we would only pick from trees [0,1].
# Example 3:
# Input: fruits = [1,2,3,2,2]
# Output: 4
# Explanation: We can pick from trees [2,3,2,2].
# If we had started at the first tree, we would only pick from trees [1,2].
# Constraints:
# 1 <= fruits.length <= 10^5
# 0 <= fruits[i] < fruits.length
# -----------------------------------------
from collections import defaultdict


# Return an int with the maximum count of fruit that can be picked
def count_fruit(fruits):
    selected_fruit = {}
    curr_count = 0
    max_count = 0
    left = 0
    right = 0
    while left < len(fruits) and right < len(fruits):
        r_fruit = fruits[right]
        l_fruit = fruits[left]

        # We know that the fruit to the right can be added
        if r_fruit in selected_fruit and len(selected_fruit) <= 2:
            selected_fruit[r_fruit] += 1
            right += 1
            curr_count += 1
        elif r_fruit not in selected_fruit and len(selected_fruit) < 2:
            selected_fruit[r_fruit] = 1
            right += 1
            curr_count += 1
        else:
            # The fruit at the right can't be added
            # Need to take away a fruit from the left
            # Assume that it was added in and can be safely taken away??
            selected_fruit[l_fruit] -= 1
            if selected_fruit[l_fruit] == 0:
                del selected_fruit[l_fruit]
            curr_count -= 1
            left += 1
        max_count = max(max_count, curr_count)

    return max_count


fruits = [1, 2, 1]
print(count_fruit(fruits))
# Output: 3

fruits = [0, 1, 2, 2]
print(count_fruit(fruits))
# Output: 3

fruits = [1, 2, 3, 2, 2]
print(count_fruit(fruits))
# Output: 4

fruits = [0]
print(count_fruit(fruits))
# Output: 1

fruits = [0, 0, 0, 1, 2, 3, 4]
print(count_fruit(fruits))
# Output: 4

fruits = [3, 2, 2, 3, 3, 2, 3, 4, 2]
print(count_fruit(fruits))
# Output: 7

fruits = [1, 5, 1, 1, 1, 2]
print(count_fruit(fruits))
# Output: 5

fruits = []
print(count_fruit(fruits))
# Output: 0

# ---------------------------------------------------------
# set doesn't work when the same fruit is listed in a row and needs to be removed
# def count_fruit(fruits):
#     selected_fruit = set()
#     curr_count = 0
#     max_count = 0
#     left = 0
#     right = 0
#     while left < len(fruits) and right < len(fruits):
#         current_right_fruit = fruits[right]
#         # Know for sure that the fruit can be added to basket, add from right
#         if current_right_fruit in selected_fruit:
#             curr_count += 1
#             right += 1
#         elif len(selected_fruit) < 2:
#             selected_fruit.add(current_right_fruit)
#             curr_count += 1
#             right += 1

#         # Can't add the fruit to the basket yet, take away from left
#         # selected_fruits is >= 2
#         else:
#             current_left_fruit = fruits[left]
#             while fruits[left] == current_left_fruit:
#                 curr_count -= 1
#                 left += 1
#             selected_fruit.remove(current_left_fruit)

#         # calculate if the current count results in new max_count
#         max_count = max(curr_count, max_count)
#     return max_count

# Dict version doesn't work
# def count_fruit(fruits):
#     selected_fruit = {}
#     curr_count = 0
#     max_count = 0
#     left = 0
#     right = 0
#     while left < len(fruits) and right < len(fruits):
#         # print(f"selected_fruit: {selected_fruit}")
#         current_right_fruit = fruits[right]
#         # Know for sure that the fruit can be added to basket, add from right
#         if current_right_fruit in selected_fruit:
#             curr_count += 1
#             right += 1
#             selected_fruit[current_right_fruit] += 1
#         if len(selected_fruit) < 2:
#             selected_fruit[current_right_fruit] = 1
#             curr_count += 1
#             right += 1

#         # Can't add the fruit to the basket yet, take away from left
#         else:
#             current_left_fruit = fruits[left]
#             selected_fruit[current_left_fruit] -= 1
#             if selected_fruit[current_left_fruit] == 0:
#                 del selected_fruit[current_left_fruit]
#             curr_count -= 1
#             left += 1

#         # calculate if the current count results in new max_count
#         max_count = max(curr_count, max_count)
#     return max_count
