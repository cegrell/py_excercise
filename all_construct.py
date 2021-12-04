from typing import List

def all_construct(target: str, word_bank: list, memo={}) -> List[List[str]]:
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
            ret = all_construct(suffix, word_bank)
            for i in range(len(ret)):
                ret[i].insert(0, word)  
            lst_collection.extend(ret)            
    memo[target] = lst_collection
    return lst_collection


print(all_construct('abcdef', ['ab', 'c', 'def', 'd', 'ef', 'e', 'f']))