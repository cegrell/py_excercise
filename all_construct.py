from typing import List

def all_construct_memo(target: str, word_bank: list, memo={}) -> List[List[str]]:
    # m lenght of target
    # b length of word_bnka
    # Time: n^m 
    # Space: m - usually dont include output in space complexity  
    if target == '': return [[]]
    if target in memo: return memo[target]

    lst_collection = []

    for word in word_bank:
        if target.find(word) == 0:
            suffix = target.replace(word, '')
            ret = all_construct_memo(suffix, word_bank)
            for i in range(len(ret)):
                ret[i].insert(0, word)  
            lst_collection.extend(ret)            
    memo[target] = lst_collection
    return lst_collection


# print() ('abcdef', ['ab', 'c', 'def', 'd', 'ef', 'e', 'f']))

def all_construct_tabulation(target: str, word_bank: list) -> list:
    tbl = [[] for _ in range(len(target) + 1)]
    tbl[0] = [[]]
    for i in range(len(target) + 1):
        for word in word_bank:
            if word == target[i:i+len(word)]:
                new_combos = [x + [word] for x in tbl[i]]
                tbl[i + len(word)] += new_combos                
    return tbl[len(target)]

print(all_construct_tabulation('abcdef', ['ab', 'c', 'def', 'd', 'ef', 'e', 'f']))
