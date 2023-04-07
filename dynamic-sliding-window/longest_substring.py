# 4:15
# Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# Constraints:
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.

# Input: a string of characters
# Output: (int) length of contiguous substring without repeating characters
def longest_substring(s):
    visited = set()
    left = 0
    right = 0
    curr_count = 0
    max_length_count = 0
    while left < len(s) and right < len(s):
        r_char = s[right]
        if r_char not in visited:
            visited.add(r_char)
            curr_count += 1
            right += 1
        else:
            l_char = s[left]
            visited.remove(l_char)
            curr_count -= 1
            left += 1
        max_length_count = max(curr_count, max_length_count)
    return max_length_count


# Example 1:
s = "abcabcbb"
print(longest_substring(s))
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
s = "bbbbb"
print(longest_substring(s))
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
s = "pwwkew"
print(longest_substring(s))
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
