def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    result = "1"
    count = 2
    while count <= n:
        next_result = get_count_and_say(result)
        count += 1
        result = next_result

    return result

# "3322251" --> "23321511"
# 2x3, 3x2, 1x5, 1x1


def get_count_and_say(numbers):
    result = ""
    current_num = numbers[0]
    current_count = 0
    for index, num in enumerate(numbers):
        if current_num != num:
            result += str(current_count) + current_num
            current_num = num
            current_count = 1
        else:
            current_count += 1
    result += str(current_count) + current_num
    return result
# print(get_count_and_say("3322251"))


print(countAndSay(1))

# Input: n = 4
# Output: "1211"
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = say "1" = one 1 = "11"
# countAndSay(3) = say "11" = two 1's = "21"
# countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
print(countAndSay(4))
