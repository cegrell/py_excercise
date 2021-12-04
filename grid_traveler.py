def grid_traveler(m: int , n: int) -> int:
    table = [[0] * (m + 1) for i in range( (n + 1))]
    table[1][1] = 1
    for i in range(n + 1):
        for j in range(m + 1):
            if j + 1 <= m: table[i][j + 1] += table[i][j] # x axis
            if i + 1 <= n: table[i + 1][j] += table[i][j] # y axis
    return table[n][m]

print(grid_traveler(3, 5))