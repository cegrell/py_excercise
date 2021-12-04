def best_sum_tabulation(target_sum: int, numbers: list) -> list:
    # Time: m^2 * n
    # Space: m^2
    lst = [None] * (target_sum + 1)
    lst[0] = []

    for i in range(target_sum + 1):
        if lst[i] is not None: 
            for n in numbers: 
                if i + n < target_sum + 1: 
                    tmp = lst[i] + [n]
                    if lst[i + n] is None or len(lst[i + n]) > len(tmp):
                         lst[i + n] = tmp
    print(lst)

best_sum_tabulation(8, [2, 3, 5, 1])