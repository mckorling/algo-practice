import itertools

def combinationSum3(k: int, n: int) -> List[List[int]]:
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    combos = itertools.combinations(nums, k)
    result = []
    for c in combos:
        if sum(c) == n:
            result.append(c)

    return result


def combinationSum3Bactrack(k, n):
    result = []
    def backtrack(remain, combo, next_start):
        if remain == 0 and len(combo) == k:
            result.append(list(combo))
            return
        elif remain < 0 or len(combo) == k:
            return
            # no match was found
        for i in range(next_start, 9):
            combo.append(i+1)
            backtrack(remain-i-1, combo, i+1)
            combo.pop()
    backtrack(n, [], 0)
    return result