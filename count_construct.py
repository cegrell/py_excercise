
def countConstruct(target: str, word_bank: list) -> int:
    # Time: O(n^m * m)
    # Space: O(m^2)
    target_len = len(target)
    if target == '': return 1         
    sums = 0
    for word in word_bank:
        word_len = len(word)
        if (word_len <= target_len) & (target[:word_len] == word ):
            suffix = target[word_len:]
            sums += countConstruct(suffix, word_bank)
    return sums


#print(countConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))


def count_construct_memized(target: str, word_bank: list, memo: dict = {}) -> int:
    # Time: O(n * m^2)
    # Space: O(m^2)
    if target == '': return 1
    if target in memo: return memo[target]
    counter = 0
    for word in word_bank:
        if target.find(word) == 0:
            suffix = target.replace(word, '')
            count = count_construct_memized(suffix, word_bank, memo)
            memo[target] = count
            counter += count
    memo[target] = counter
    return counter

#print(count_construct_memized('abcdef', ['abc', 'a', 'bc', 'def', 'd', 'ef']))


def count_construct_tabulation(target: str, word_bank: list) -> int:
    # m target
    # n wordbank length
    # Time: O(m^2 * n)
    # Space: m 
    tbl = [0] * (len(target) + 1)
    tbl[0] = 1

    for i in range(len(target)):
        for word in word_bank:
            if target[i] == word[0]:
                if i + len(word) < len(tbl):
                    tbl[i+len(word)] += tbl[i]
    return tbl[len(target)]    


print(count_construct_tabulation('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
