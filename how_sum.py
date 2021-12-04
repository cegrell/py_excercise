def how_sum(target_sum: int, nums: list) -> list:
    # m = targetSum
    # n - len(nums)
    # Time = O(n^m * m) Due to the appending part (makes a linear copy)
    # Space: O(m)
    if target_sum == 0: return []
    if target_sum < 0: return None

    for n in nums:
        remainder = target_sum - n
        ret = how_sum(remainder, nums)
        if ret is not None:
            return ret + [n]
        
    return None

def how_sum_memoized(target_sum: int, nums: list, memo: dict = {}) -> list:
    # This is a memoized version
    # Time: O(n*m*m) = O(n*m^2) where n is the width, first m is the height of tree, 
    # and second m is the list copying action 
    # Space: O(m*m) = O(m^2) where m is for the height and extra array
    if target_sum in memo: return memo[target_sum]
    if target_sum == 0: return []
    if target_sum < 0: return None

    for n in nums:
        remainder = target_sum - n
        ret = how_sum_memoized(remainder, nums, memo)
        if ret is not None:
            memo[target_sum] = ret + [n] 
            return memo[target_sum]
    memo[target_sum] = None
    return None



# print(howSum_memoized(300, [7, 14]))

def how_sum_tabulation(target_sum: int, nums: list) -> list:
    tbl = [None] * (target_sum + 1)
    tbl[0] = []

    for i in range(target_sum + 1):
        if tbl[i] is not None:
            for n in nums:
                if i + n < target_sum + 1: tbl[i + n] = tbl[i] + [n]
    return tbl[target_sum]

print(how_sum_tabulation(7, [5, 3, 4]))