def howSum(targetSum: int, nums: list) -> list:
    # m = targetSum
    # n - len(nums)
    # Time = O(n^m * m) Due to the appending part (makes a linear copy)
    # Space: O(m)
    if targetSum == 0: return []
    if targetSum < 0: return None

    for n in nums:
        remainder = targetSum - n
        ret = howSum(remainder, nums)
        if ret is not None:
            return ret + [n]
        
    return None

def howSum_memoized(targetSum: int, nums: list, memo: dict = {}) -> list:
    # This is a memoized version
    # Time: O(n*m*m) = O(n*m^2) where n is the width, first m is the height of tree, 
    # and second m is the list copying action 
    # Space: O(m*m) = O(m^2) where m is for the height and extra array
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return []
    if targetSum < 0: return None

    for n in nums:
        remainder = targetSum - n
        ret = howSum_memoized(remainder, nums, memo)
        if ret is not None:
            memo[targetSum] = ret + [n] 
            return memo[targetSum]
    memo[targetSum] = None
    return None



print(howSum_memoized(300, [7, 14]))