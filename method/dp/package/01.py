# coding=utf-8


def method_1(n, c, weights, values):
    dp = []
    for _ in range(c+1):
        dp.append([0]* (n+1))
    
    for i in range(1, c+1):  # 先遍历容量
        for j in range(1, n+1):  # 再遍历物品数量
            if i<weights[j-1]:
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = max(dp[i-weights[j-1]][j-1] + values[j-1], dp[i][j-1])
    return dp[c][n]


def method_2(n, c, weights, values):
    dp = []
    for _ in range(n+1):
        dp.append([0]*(c+1))
    
    for i in range(1, n+1): # 先遍历物品
        for j in range(1, c+1):   # 再遍历容量
            if weights[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j-weights[i-1]]+values[i-1], dp[i-1][j])
    return dp[n][c]


if __name__ == '__main__':
    weights = [10, 20, 30, 40 ,50]
    values = [50, 120, 150, 210, 240]
    n= 5
    c=50
    res_1 = method_1(n, c, weights, values)
    res_2 = method_2(n, c, weights, values)
    print(res_1, res_2)
