def canSum(targetSum: int, numbers: list) -> bool:
    # Time complexity would be n^m where n is the elements in numbers,
    # and m is the levels of the tree, ie targetSum.
    # Space complexity would be m, ie the height of the tree
    if targetSum == 0: return True
    if targetSum < 0: return False

    for n in numbers:
        remainder = targetSum - n        
        if canSum(remainder, numbers) == True:
            return True
    return False


def canSum_memoised(targetSum: int, numbers: list, memo: dict = {}) -> bool:
    # m is targetSum, n is array length
    # Time complexity: O(m * n)
    # Space complexity: O(m)
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return True
    if targetSum < 0: return False

    for n in numbers:
        remainder = targetSum - n        
        if canSum(remainder, numbers, memo) == True:
            memo[targetSum] = True        
            return True
    memo[targetSum] = False
    return False


print(canSum(7, [2, 3], {})) # true
print(canSum(7, [5, 3, 4, 7], {})) # true
print(canSum(7, [2, 4], {})) # false
print(canSum(8, [2, 3, 5], {})) # true
print(canSum(300, [7, 14], {})) # false