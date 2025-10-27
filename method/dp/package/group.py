# coding=utf-8

def main(n, c, weights, values):
    dp = []
    for _ in range(n+1):
        dp.append([0]*(c+1))
    
    for i in range(1, n+1):
        for j in range(1, c+1):
            num = len(weights[i-1])
            print(i, j, num)
            for k in range(num):
                if weights[i-1][k] > j:
                    dp[i][j] = max(dp[i-1][j], dp[i][j])  # 由于要迭代多次，所以要和当前状态 dp[i][j] 做比较
                else:# 由于要迭代多次，所以要和当前状态 dp[i][j] 做比较
                    dp[i][j] = max(max(dp[i-1][j-weights[i-1][k]] + values[i-1][k], dp[i-1][j]), dp[i][j])
    return dp[n][c]


if __name__ == '__main__':
    n = 3
    c = 10
    weights = [
        [2, 3],
        [4, 6],
        [2, 3]
    ]
    values = [
        [1, 3],
        [8, 9],
        [8, 9]
    ]
    res = main(n, c, weights, values)
    print(res)
