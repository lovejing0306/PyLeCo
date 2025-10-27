# coding=utf-8

def main(n, c, weights, values):
    dp = []
    for _ in range(n+1):
        dp.append([0]*(c+1))

    for i in range(1, n+1):
        for j in range(1, c+1):
            if weights[i-1] > j:
                dp[i][j] = dp[i-1][j]  # 如果物品重量大于当前的背包重量，则取 i-1 的物品数量时的结果
            k=1
            while k * weights[i-1] <= j:  # 当物品总重量超出背包重量时，则不在放置
                dp[i][j] = max(dp[i-1][j-weights[i-1]*k] + values[i-1]*k, dp[i-1][j])
                k+=1
    return dp[n][c]


if __name__ == '__main__':
    weights = [10, 20, 30, 40 ,50]
    values = [50, 120, 150, 210, 240]
    n= 5
    c=50
    res = main(n, c, weights, values)
    print(res)
