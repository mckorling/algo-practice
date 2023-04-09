# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
# frequency
#  of at least one of the chosen numbers is different.
def combinationSum(candidates, target: int):
    results = []

    def backtrack(remainder, combo, start):
        if remainder == 0:
            # found a valid condition
            results.append(list(combo))
            return
        elif remainder < 0:
            # not valid, return to keep backtracking
            return

        for i in range(start, len(candidates)):
            combo.append(candidates[i])
            backtrack(remainder-candidates[i], combo, i) # can reuse a number
            combo.pop() # remove a number to backtrack and try the next number  
    
    backtrack(target, [], 0)
    return results

candidates = [2,3,6,7]
target = 7
print(combinationSum(candidates, target))

candidates = [2,3,5]
target = 8
print(combinationSum(candidates, target))