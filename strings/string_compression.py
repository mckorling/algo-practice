# leetcode: 443, Medium
# https://leetcode.com/problems/string-compression/description/
# Stupid description that is just not possible to understand
# So I will modify it
# Given an input list of chars, compress the string so that:
# Input: chars = ["a","a","b","b","c","c","c"]
# Output: "a2b2c3"
# Input: chars = ["a"]
# Output: "a"
# Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output: "ab12"

def compress(chars):
    """
    :type chars: List[str]
    :rtype: int
    """
    s = ""
    current = chars[0]
    count = 1
    for i in range(1, len(chars)):
        if chars[i] != current:
            s += current
            if count > 1:
                s += str(count)
            current = chars[i]
            count = 1
        else:
            count += 1
    s += current
    if count > 1:
        s += str(count)
    return s


chars = ["a", "a", "b", "b", "c", "c", "c"]
print(compress(chars))
# Output: "a2b2c3"

chars = ["a"]
print(compress(chars))
# Output: "a"

chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
print(compress(chars))
# Output: "ab12"
