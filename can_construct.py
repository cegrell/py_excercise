def can_construct(target: str, word_bank: list) -> bool:
    if target == '': return True
    target_length = len(target)
    for word in word_bank:
        w_len = len(word)
        if w_len > target_length:
            continue
        if target[:w_len] == word:
            if can_construct(target[w_len:], word_bank) is True:
                return True
        elif target[w_len:] == word:
            if can_construct(target[:w_len], word_bank) is True:
                return True
    return False


print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))

