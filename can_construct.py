def can_construct(target: str, word_bank: list) -> bool:
    # n = elements in word_bank - the branching factor
    # m = target length, number of levels 
    # Time: n^m * m
    # Space: m^2 - since we're creating slices for each level in the tree 
    if target == '': return True
    target_length = len(target)
    for word in word_bank:
        w_len = len(word)
        if w_len > target_length:
            continue
        if target[:w_len] == word:
            if can_construct(target[w_len:], word_bank) is True: # This line adds to the time complexity with *m
                return True # above line creates a new string, which will be dependent on m, thus creating m * m
        elif target[w_len:] == word:
            if can_construct(target[:w_len], word_bank) is True:
                return True
    return False


#print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'ab', 'abc', 'cd', 'def', 'abcd']))

def can_construct_optimised(target: str, word_bank: list, memo: dict = {}) -> bool:
    # With memoization
    # m is len(target)
    # n is len(word_bank)
    # Time: O(n * m^2) - the second m
    # Space: (m^2)


    if target == '': return True
    if target in memo: return memo[target]
    target_length = len(target)
    for word in word_bank:
        w_len = len(word)
        if w_len > target_length:
            continue
        if target[:w_len] == word:
            if can_construct_optimised(target[w_len:], word_bank, memo) is True:
                memo[target] = True
                return True 
        elif target[w_len:] == word:
            if can_construct_optimised(target[:w_len], word_bank, memo) is True:
                memo[target] = True
                return True
    memo[target] = False
    return False

# print(can_construct_optimised('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee', ['e', 'ee', 'eee', 'ab', 'abc', 'cd', 'def', 'abcd']))
#print(can_construct_optimised('abcdefe', ['ab', 'abc', 'cd', 'def', 'abcd']))

def can_construct_tabulation(target: str, word_bank: list) -> bool:
    tbl = [False] * (len(target) + 1)
    tbl[0] = True # seed value

    for i in range(len(target)):
        if tbl[i] is True:
            for word in word_bank:
                # Check if word matches the chars starting at position i
                if target[i: i + len(word)] == word:
                    tbl[i + len(word)] = True
    return tbl[len(target)]


print(can_construct_tabulation('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))